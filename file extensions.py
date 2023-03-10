fileName = input("enter file name: ")
fileTypeExtention = fileName.rsplit(".")


match fileTypeExtention[1]:
    case "gif": 
        print("Image/gif")
    case "jpg":
        print("Image/jpg")
    case "jpeg":
        print("Image/jpeg")
    case "png":
        print("Image/png")
    case "pdf":
        print("Application/pdf")
    case "txt":
        print("Text File/Document")
    case "zip":
        print("Archive")
    
