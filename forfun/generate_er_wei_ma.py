from MyQR import myqr        # 注意区分大小写
import qrcode
'''
博客地址：https://cloud.tencent.com/developer/article/1629725
myqr生成二维码样例
'''
# myqr.run(words='hello world')   # 生成二维码，只能支持英文
# myqr.run(
#     words='http://www.baidu.com',    # 包含信息
#     picture='lbxx.jpg',            # 背景图片
#     colorized=True,            # 是否有颜色，如果为False则为黑白
#     save_name='code.png'    # 输出文件名
# )

# 生成二维码
# img = qrcode.make(data="范秀莲，你好！")
# # 将二维码保存为图片
# with open('test.png', 'wb') as f:
#     img.save(f)
#
qr = qrcode.QRCode(
    version=5,        # 二维码的大小，取值1-40
    box_size=10,    # 二维码最小正方形的像素数量
    error_correction=qrcode.constants.ERROR_CORRECT_H,    # 二维码的纠错等级
    border=5    # 白色边框的大小
)
qr.add_data('https://colagold.github.io/')    # 设置二维码数据
img = qr.make_image()    # 创建二维码图片
img.save('qrcode.png')    # 保存二维码