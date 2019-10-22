#-*- coding:utf-8 -*-

# 倒包
from appium import webdriver
# 导入休眠包
import time
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')

# 声明字典,将需要指定的属性加进来

qiezzi = {}

# 手机的版本号 注意这里的版本号写你将要运行到手机上的版本号
qiezzi['platformVersion']="4.4"
# 指定工具是安卓还是ios
qiezzi['platformName']="Android"
# 指定手机的唯一识别码 通过 adb devices 来获取手机唯一识别码,前提是手机必须链接上电脑,而且开启usb调试模式
# 如果手机连接不上电脑,我们通过命令安装 adb connect 唯一识别吗,这种情况针对的是以前链接过的,我们知道唯一识别吗
# 如果以前不知道只能通过360手机助手去链接,或者通过开发工具as运行去安装手机驱动
qiezzi['deviceName'] = "127.0.0.1:21503"
# 指定需要安装apk路径
qiezzi['app'] = "E:\qieziapk\com.qiezzi.eggplant.apk"
# 指定app启动和等待的包名
# 我们要获取包名,在公司里面一般都是自己反编译,也可以问开发,
# 首先我们需要一个反编译的包: AXMLPrinter2.S.jar,来帮助我们进行反编译
# 首先第一步,将我们的apk,设置为zip方式,进行解压,
# 其次将 AXMLPrinter2.S.jar 放在我们需要反编译的文件的平行层,比如我们需要反编译mainfest.xml文件,就放到和他平行层
# 通过命令行进入带这一层文件,输入命令 java -jar AXMLPrinter2.S.jar 需要反变压的文件(AndroidManifest.xml) > (表示到那个文件) AndroidManifest1.xml
qiezzi['appPackage']='com.qiezzi.eggplant'
# 指定app等待的时候的包名
qiezzi['appWaitPackage']='com.qiezzi.eggplant'
# 获取安卓里面默认启动的activity,需要通过inflter
# 设置需要启动的activity的名字 activity可以写成绝对的,也可以写成相对的
# 相对的写法, 用.代表包名,后面直接写寄丢可以了
# 绝对路径,直接从包名写起
qiezzi['appActivity']='com.qiezzi.eggplant.base.WelcomeActivity'
# 设置等待启动的activity
qiezzi['appWatiActivity']='com.qiezzi.eggplant.base.WelcomeActivity'

# 启动app
# 注意如果报一下错误,说明你的url,不符合http请求格式
# URLError: <urlopen error unknown url type: 127.0.0.1>
# http 请求格式 http://(请求头) + ip:端口号(模拟这两个在正式环境用域名代替了,默认端口号80不用写)+路径

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",qiezzi)


# 以上几步就可以把app启动起来

# 设置休眠
time.sleep(5)

# 滑动, 滑动的命令 swipe 里面有五个参数
# 1: 滑动开始的x位置
# 2: 滑动开始的y轴位置
# 3: 滑动结束的x轴位置
# 4: 滑动结束的Y轴位置
# 5: 滑动的持续时间
# 注意 安卓手机的x,y周的圆点在手机的左上角

# 获取手机屏幕的宽度和高度,返回的是字典
print driver.get_window_size()

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']

print width,height

# 现在流行的手机 无边框手机,因为咱们的手机有边框,所以我们不能从手机的宽度开始滑动,我们给他减去 50

driver.swipe(width-50,height/2,50,height/2,1000)

# 休眠 2秒
time.sleep(2)

driver.swipe(width-50,height/2,50,height/2,1000)

# 休眠 2秒
time.sleep(2)

driver.swipe(width-50,height/2,50,height/2,1000)

# 休眠 2秒
time.sleep(2)

# 点击立即体验按钮
btn_feel_right_now = driver.find_element_by_id("com.qiezzi.eggplant:id/btn_feel_right_now")

btn_feel_right_now.click()

time.sleep(2)

# 关闭客户端
driver.quit()


