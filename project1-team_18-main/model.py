from torch import nn, optim
import torch.nn.functional as F
from torchvision.transforms import transforms

#<Quick Start PyTorch(2)--how to build a neural network>
#https://blog.csdn.net/weixin_33798152/article/details/91417595
class Net(nn.Module):  # neural network design
    def __init__(self):  # setup on init, defining layers
        super(Net ,self).__init__()
        self.input = nn.Linear(28 *28, 256)  # input layer
        self.h1 = nn.Linear(256, 128)  # hidden layers
        self.h2 = nn.Linear(128, 128)  # //
        self.h3 = nn.Linear(128, 64)  # //
        self.output = nn.Linear(64, 62)  # output layer
        self.dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's', 55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'}
        self.transform = transforms.Compose([transforms.Resize((28,28)),transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,)),])
    
    #<Quick Start PyTorch(2)--how to build a neural network>
    #https://blog.csdn.net/weixin_33798152/article/details/91417595
    #<[pytorch study notes] Part 4 - Neural Network>
    #https://blog.csdn.net/QLeelq/article/details/120711804
    def forward(self, img):
        convflat = img.view(-1,  784)  # flatten tensor
        convflat = F.relu(self.input(convflat))  # pass tensor through linear layers via ReLU function
        convflat = F.relu(self.h1(convflat))  # //
        convflat = F.relu(self.h2(convflat))  # //
        convflat = F.relu(self.h3(convflat))  # //
        return self.output(convflat)  # output tensor, now size 10
    #<YOLOV3 target detection implementation based on OpenCV DNN>
    #http://aiuai.cn/aifarm962.html 
    #<PyTorch/[PyTorch study notes] 2.2 Image preprocessing transforms module mechanism>
    #https://blog.zhangxiann.com/202002212045/
    #<torch. nn.Softmax(dim=1)>
    #https://blog.csdn.net/m0_37859875/article/details/108729911
    def predict(self,img):
        x = self.transform(img)
        x = self.forward(x).softmax(dim=1)
        index = x.argmax().item()
        return self.dict[index],x[0][index].item() # return the index of the max value in the output tensor
# model = Net()  # assign Net() to var
# model.to(device)  # move model to device
# criterion = nn.CrossEntropyLoss()  # define loss type
# optimiser = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)  # define optimiser

