import pyttsx3


class Sound:
    # 传入主对象
    def __init__(self, calc):
        self.calc = calc

    # 初始化语音
    def sound_init(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        for item in voices:  # 寻找英文语音支持
            s = str(item.id)
            if 'EN-US' in s:
                self.engine.setProperty("voice", s)
                return "Ok"
        return "Error"


    # 语音
    def make_voice(self):
        text = self.calc.textBrowser.toPlainText()
        text = text.replace('-', "minus")
        text = text.replace('!', "factorial")
        text = text.replace('^', "power")
        text = text.replace('√', "root")
        text = text.replace('.', "dot")
        self.engine.say(text)
        self.engine.runAndWait()
