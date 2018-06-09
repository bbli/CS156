# Pytorch
=======

## Variables and Operations
---

> Torch Variables hold **weights** and a reference to **computational graph**
    * Gives us autograd capabilities -> `loss.backwards()`, which calculates gradients and stores them in  `TorchVariable.grad.data`

> As you multiply Pytorch variables, a computational graph is being defined as a **side effect**.
    * A computational graph is a directed graph where the links are functions on the tensors and nodes are Pytorch variables.

> data needs to be **wrapped** in a **pytorch Variable**, and not just a pytorch tensor
    * Because weights are Pytorch Variables, and you cannot multiply variables and tensors
    
* Ohh, so you only need to define your own autograd function with a backwards method if you don't stick to **Pytorch operations**.
* Indexing is a **valid** pytorch operation, assuming you are not indexing to modify an array in place
* Huh, so my hypothesis for how Pytorch handles minibatches without calling backwards multiple times is by creating several nodes from the output nodes, one node for each sample in the minibatch.
    * wait, arn't minibatches handles by matrix-matrix multiplication?
* On the other hand, multiple trajectories can be handled by combining the multiple computational graphs to create one large computational graph


* Pytorch always assumes minibatches. So for example, you would need to enter a 2 dimensional matrix into a linear model
## Model attributes
---
* Define your models as a parent to `nn.Module` so you inherit methods like `forward` 
* Most pytorch operations will have a inplace and out of place version
    * default is out of place as time>space

## Acessing model's weights
* `model.parameters()` to get a generator of the model's weights
    * pytorch variables in your class will not show up when you call `model.parameters()`
    * all pytorch `Variables` created from pytorch `Modules` get labeled as pytorch `Parameters`
    * `model.named_parameters()`to get a generator of the model's weights with names
* `model.state_dict()` to get all the weights at once
* Note you can also acess weights through the optimizer.




## 1. PreProcessing
---
* Note you should be defining a "train" and "val" DataSet, Transform, and DataLoader objects

### DataSet
* to create your own Dataset class, overwrite two methods from base class `Dataset`
    * __len__
    * __getitem__ -> this allows you to use indexing!
        * __getitem__ must return an image and label in torchTensor format
* __init__ usually has transform object as argument
    * used on every __getitem__ call(or in __init__ if you have the space)

**Transform**
* To define your own transform Class, just give it a `__call__` method, as `transform.Compose` will call that in the pipeline
* `RandomFlip` data augments by **replacing** original image, rather than appending.

### DataLoader: `DataLoader(transformed_dataset, batch_size=4, shuffle=True)`
* will create a iterator(not iterable) that returns **batches**
* The images returned from the dataset class needs to be 3D Pytorch tensor of the form `(C,X,Y)`. The Dataloader will make it into `(N,C,X,Y)`

## 2. The Model 
---
> Hmm, so pytorch way is to just have the class hold the network function and all the data. Loss, backprop, display, are all outside functions

### Layers
* torch.nn Layers will only accept minibatches, instead of a single sample.
    * use `pytorch_tensor.unsqueeze(0)` to add another dimension to the data
**Conv2d**
* kernel_size: the convolution filter
* stride: controls step size of kernel movement
* dilation: controls spacing for convolution action
* padding: number of extra squares on both sides for each dimension
* out_channels: number of output features

* bias: default true
* in_channels: number of input features
**MaxPool2d**
* kernel_size: size of maxpooling
* stride: default value is the kernel_size
* padding:

* dilation: 
* return indices: returns indexes of the max number. 
    * useful for Unpooling
* ceil_mode
**Dropout2d**
used for the convolutional layer instead of the fully connected part
apprantly it will help promote independence between feature maps -> less convolutions layers needed
### Autograd Functions
* Just need to define a forward and backward pass, which is what needs to be computed during backpropagation.
    * definig the backwards is probably painful, so I will rarely do this.
```
import torch
from torch.autograd import Variable

class MyReLU(torch.autograd.Function):
  """
  We can implement our own custom autograd Functions by subclassing
  torch.autograd.Function and implementing the forward and backward passes
  which operate on Tensors.
  """
  def forward(self, input):
    """
    In the forward pass we receive a Tensor containing the input and return a
    Tensor containing the output. You can cache arbitrary Tensors for use in the
    backward pass using the save_for_backward method.
    """
    self.save_for_backward(input)
    return input.clamp(min=0)

  def backward(self, grad_output):
    """
    In the backward pass we receive a Tensor containing the gradient of the loss
    with respect to the output, and we need to compute the gradient of the loss
    with respect to the input.
    """
    input, = self.saved_tensors
    grad_input = grad_output.clone()
    grad_input[input < 0] = 0
    return grad_input
```

### Defining the Model
**weight initalization**
```
class MyModel(nn.Module):
    def __init__(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
m.bias.data.zero_()
```
**freezing layers**
```
x = Variable(torch.randn(5, 5), requires_grad=True) # this Variable can no longer have its value updated
y = Variable(torch.randn(5, 5), volatile=True) #this will make all foward operations from the variable also frozen
```



## 3. Training
---
### Objects
**Optimizer**: `optimizer = torch.optim.SGD(model.parameters(), lr=0.01)`

> `optimizer.step()` will decide how to update the model based on the gradient, which is calcuated in the `loss.backwards()` part of the code.

* differential learning rates is probably done by:
    1. defining groups in `optimizer.param_groups`. How do I label the layers though?
    2. Using the LambdaR method from `torch.optim.lr_scheduler` 
    OR
    ```
    optim.SGD([
                {'params': model.base.parameters()},
                {'params': model.classifier.parameters(), 'lr': 1e-3}
            ], lr=1e-2, momentum=0.9)
    ```
* optimizer.param_groups will create a dictionary of the weights and hyperparameters, with each layer being a seperate element in a list
* `optimizer.param_groups` returns the optimizer parameters and the model's parameters
* `optimizer.state_dict()` returns **A COPY** of the **current** optimizer parameters and the optimizer's "state"


**Scheduler**: `scheduler = lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)`
* scheduler will wrap a optimizer and change the learning rate based on a "schedule"
* instead of `optimizer.step` you do `scheduler.step()`
### Training Loop

> make sure to zero the gradients
* pytorch will free the gradient buffers after the `node.backwards()` call.

```
for epoch in range(epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target)
        # resize data from (batch_size, 1, 28, 28) to (batch_size, 28*28)
        data = data.view(-1, 28*28)
        optimizer.zero_grad()
        net_out = net(data)
        loss = criterion(net_out, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset),
                           100. * batch_idx / len(train_loader), loss.data[0]))
```




## Other Pytorch Objects
---
## Tensorboard
* Each SummaryWriter will show up as a "run" in tensorboard
* To log multiple plots onto the same graph, use `add_scalars`
    * so "Accuracy" and "Loss" are seperate writes, while "Relative weight update" all goes into one

* Apparantly creating histograms take a long time.

### Sequential
* `nn.Sequential` to define layers of a neural network
```
net = nn.Sequential(
    nn.Linear(28*28, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
).cuda()
```
### ModuleList
* for storing a list of models/layers. 
    * idk how to really use this atm. Just don't use Python lists


## Things I don't quite understand
---
* pytorch training mode is a way to change the model between train time and predict time versions with no rewriting of code.
    * I suppose pytorch Dropout object checks this option
    * How to define a Module that changes based on the mode????????
    * turn on the volatile flag here??

