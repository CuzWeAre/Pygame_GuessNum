from PIL import Image

# 打开图片
image = Image.open("input.png")

# 将图片转为RGBA模式
image = image.convert("RGBA")

# 获取图片的像素数据
pixels = image.load()

# 遍历每个像素点
for y in range(image.height):
    for x in range(image.width):
        r, g, b, a = pixels[x, y]

        # 计算像素点的灰度值
        gray = int(0.2989 * r + 0.587 * g + 0.114 * b)

        # 判断是否为彩色像素
        if (r, g, b) != (gray, gray, gray):
            # 计算反色值
            inverted_r, inverted_g, inverted_b = 255 - r, 255 - g, 255 - b

            # 设置像素点的颜色为反色
            pixels[x, y] = (inverted_r, inverted_g, inverted_b, a)

# 保存处理后的图片
image.save("output.png")
