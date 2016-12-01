testFile = "test.txt"
testingFile = "test2.txt"

file2 = open(testingFile, "w")
file = open(testFile, "w")
file.write("test")
file2.write("testing writing another thing")
file.close()
file2.close