import numpy as np
import torch
from torchvision import datasets, transforms
from model import Net
device = torch.device("cpu" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,)), ])
emnist_test = datasets.EMNIST(root='./data', split='byclass', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(emnist_test, batch_size=4, shuffle=True, num_workers=2)
DNN = Net().to(device)
optimiser = torch.optim.Adam(DNN.parameters(), lr=0.0001)
criterion = torch.nn.CrossEntropyLoss()


def train(epoch,batch_size): #takes input epoch to determine what training cycle the model is on, mainly for diagnostic purposes
    # <PyTorch Deep Learning Practice Lecture 9 Multi-classification problem Handwritten digit recognition (training + testing) Super detailed>
    #https://blog.csdn.net/weixin_62321421/article/details/121435225
    ''' train the model'''
    DNN.train() #sets model in training mode
    emnist_train = datasets.EMNIST(root='./data', split='byclass', train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(emnist_train, batch_size=batch_size, shuffle=True, num_workers=2)

    if(epoch == None):
        pass
    elif(trainloader == None):
        pass
    else:
        #<PyTorch learning - summary (3) - the most practical part>
        #https://www.cnblogs.com/minyuan/p/13969547.html
        for batch_idx, (traindata, traintarget) in enumerate(trainloader): #for/enumerate loop to grab data + label
            print(batch_idx)
            traindata, traintarget = traindata.to(device), traintarget.to(device) #passes data to device
            optimiser.zero_grad() #removes gradients
            trainoutput = DNN(traindata) #pass data through model
            trainloss = criterion(trainoutput, traintarget) #calculate training loss
            trainloss.backward() #apply loss backwards to adjust weights
           #<The role of optimizer optimizer>
           #https://www.csdn.net/tags/NtzaQg0sMDc1NzAtYmxvZwO0O0OO0O0O.html
            optimiser.step() #optimises process
        print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
            epoch, batch_idx * len(traindata), len(trainloader.dataset),
            100. * batch_idx / len(trainloader), trainloss.item()))
        test()

def test(): #takes no input, tests the model against the EMNIST test dataset
    ''' test model on test dataset '''
    DNN.eval() #sets model in evaluation mode
    test_loss = 0
    correct = 0
    with torch.no_grad(): #prevents gradients from being calculated
        #<with torch.no_grad() Detailed explanation>
        #https://blog.csdn.net/weixin_46559271/article/details/105658654
        #<torch.no_grad and validation mode>
        #https://blog.csdn.net/weixin_40548136/article/details/105122989 
        #<PyTorch learning - summary (3) - the most practical part>
        #https://www.cnblogs.com/minyuan/p/13969547.html
        for data, target in testloader:
            data, target = data.to(device), target.to(device)
            output = DNN(data)
            test_loss += criterion(output, target).item() #sum up batch loss
            pred = output.argmax(dim = 1, keepdim = True) #get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item() #compare prediction to target
    test_loss /= len(testloader.dataset)
    print('\nTest set: Average loss: {:.6f}, Accuracy: {}/{} ({:.3f}%)\n'.format(
        test_loss, correct, len(testloader.dataset),
        100. * correct / len(testloader.dataset)))
    return test_loss, correct, len(testloader.dataset)
if __name__ == '__main__':

    #Pytorch study notes three deep neural network DNN
    #https://blog.csdn.net/qq_43165081/article/details/108189129
    for epoch in range(0, 1):
        train(epoch,batch_size=4)
    test()
    torch.save(DNN.state_dict(), './model.pth')
    print('Model saved')
