
class Utils:
    def formatString(self, string):
        new = string.replace('!', '')
        print(new)

if __name__ == "__main__":
    Utils.formatString('Wow! Cool Album!')