class Tag:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, cls):
        cls.tag = self.tag
        return cls

@Tag('smoke')
class SmokeTests:
    pass

@Tag('regression')
class RegressionTests:
    pass

print(SmokeTests.tag)  # smoke
print(RegressionTests.tag)  # regression
