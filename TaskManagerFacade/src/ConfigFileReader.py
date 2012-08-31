from ConfigParser import ConfigParser 


class ConfigFileReader:
    configFilePath = '..\ConfigSample.txt'
    CONFIGFILE = ConfigParser()
    def getAttribute(self,field,atr):
        self.CONFIGFILE.read(self.configFilePath)
        return self.CONFIGFILE.get(field,atr)



