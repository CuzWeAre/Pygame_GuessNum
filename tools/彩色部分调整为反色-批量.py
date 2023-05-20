from PIL import Image
import os

# 定义文件夹路径
folder_path = "D:\PycharmProjects\pygame_guessnum\images"  # 将 'folder_path' 替换为你的文件夹路径

# 获取文件夹中所有的.bmp文件
bmp_files = [file for file in os.listdir(folder_path) if file.endswith('.bmp')]

# 循环处理每个.bmp文件
for file_name in bmp_files:
    # 打开图像文件
    image_path = os.path.join(folder_path, file_name)
    image = Image.open(image_path)
    
    # 将图像转换为RGBA模式，方便处理透明通道
    image = image.convert('RGBA')
    
    # 获取图像像素数据
    pixels = image.load()
    width, height = image.size
    
    # 循环遍历图像的每个像素
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # 判断像素是否为黑白部分，黑白部分保持不变，彩色部分进行反色处理
            # if a == 0:
            #     pixels[x, y] = (0, 0, 0, 0)
            # elif r == g == b or (r + g + b) / 3 > 220:
            #     # 黑白部分不变
            #     pixels[x, y] = (0, 0, 0, 0)
            # else:
            #     # 彩色部分反色处理
            #     pixels[x, y] = (255 - r, 255 - g, 255 - b, a)
                
            # 绿色改成反色
            if g > r and g > b:
                pixels[x, y] = (255 - r, 255 - g, 255 - b, a)
            else:
                pixels[x, y] = (r, g, b, 0)
                
            
    # 保存处理后的图像为.bmp文件
    output_path = os.path.join(folder_path, file_name.split('.')[0] + '_reversed.bmp')
    image.save(output_path, 'BMP')

print('处理完成！')
