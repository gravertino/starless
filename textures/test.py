# 测试resize命令是否正常运行
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import imageio as spm
input = spm.imread('textures/bgedit.jpg')
output = np.array(Image.fromarray(input, mode="RGB").resize((int(2*input.shape[1]),int(2*input.shape[0])), resample=Image.BICUBIC))
plt.imshow(output)
plt.show()