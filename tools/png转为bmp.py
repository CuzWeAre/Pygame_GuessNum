import os
from PIL import Image
folder_path = "F:\Desktop\新建文件夹"  # 替换为实际的文件夹路径
target_format = ".bmp"

def convert_to_bmp_with_transparency(image):
    # 创建一个新的RGBA模式的图像，大小与原图像相同
    new_image = Image.new("RGBA", image.size)

    # 获取原图像的像素数据
    pixels = image.load()

    # 遍历每个像素
    for i in range(image.width):
        for j in range(image.height):
            # 获取当前像素的RGBA值
            r, g, b, a = pixels[i, j]

            # 如果当前像素的alpha通道值为0，则在新图像中保持透明
            if a == 0:
                new_image.putpixel((i, j), (0, 0, 0, 0))
            else:
                new_image.putpixel((i, j), (r, g, b, 255))

    return new_image

for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # 构建输入文件的完整路径
        input_path = os.path.join(folder_path, filename)

        # 构建输出文件的完整路径
        output_path = os.path.join(folder_path, os.path.splitext(filename)[0] + "." + target_format)

        # 打开并转换图像格式，并保持无色部分
        image = Image.open(input_path).convert("RGBA")
        new_image = convert_to_bmp_with_transparency(image)
        
        # new_image = new_image.resize((128,128))
        
        new_image.save(output_path, format=target_format)

        print(f"Converted {filename} to {target_format}")
