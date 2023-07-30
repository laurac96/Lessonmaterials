def wrapperfunction():
    def innerfunction():
        print("Hello, I'm inside the function")
    return innerfunction()

examplefunction = wrapperfunction()
#the examplefunction because the innerfunction result in this case

examplefunction()