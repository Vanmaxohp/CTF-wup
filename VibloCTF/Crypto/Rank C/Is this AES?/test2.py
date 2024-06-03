def unique_characters(s):
    # Tạo một từ điển để đếm số lần xuất hiện của mỗi ký tự
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # In ra các ký tự chỉ xuất hiện 1 lần
    unique_chars = [char for char in s if char_count[char] == 1]
    
    return unique_chars

# Đọc chuỗi đầu vào từ người dùng
input_string = "abcdedfbgghfidecdefdhjcikdclmcdnmopdclidaqmridcleksfdekdclidhtudcmtifdmkudfhksfdefdmurikcbqifvdmfdedbfiudchdwmttdclixpdedbfiudchdclekydclmcdcliodniqidcleksfdclidnhkuiqjbtdjhtydhjdclidfchqeifdnikcdhbcdmkudthhyiudjhqvdaiwmbfidcliodnmkciudclixvdaiwmbfidcliodniqidizweceksdmkudtejidnmfdmdaecdubttvdmdyekudhjdmdfghqcvdmfdohbdxeslcdfmopdabcdclmcdefdkhcdclidnmodhjdecdnecldclidcmtifdclmcdqimttodxmcciqiuvdhqdclidhkifdclmcdfcmodekdclidxekupdjhtydfiixdchdlmridaiikd1bfcdtmkuiudekdclixvdbfbmttod2dclieqdgmclfdniqidtmeudclmcdnmovdmfdohbdgbcdecpdabcdedizgiwcdcliodlmudthcfdhjdwlmkwifvdteyidbfvdhjdcbqkeksdamwyvdhktodcliodueudkhcpdmkudejdcliodlmuvdnidflhbtudkhcdykhnvdaiwmbfidcliodnhbtudlmridaiikdjhqshccikpdnidlimqdmahbcdclhfidmfd1bfcdnikcdhkd2dmkudkhcdmttdchdmdshhudikudwqogch3khc4m4fbafcecbcehk4wegliq5vdxekudohbpdmcdtimfcdkhcdchdnlmcdjhtydekfeuidmdfchqodmkudkhcdhbcfeuidecdwmttdmdshhudikupdohbdykhnvdwhxeksdlhxivdmkudjekueksdcleksfdmttdqeslcvdclhbsldkhcd6becidclidfmxid2dteyidhtudxqpdaetahpdabcdclhfidmqidkhcdmtnmofdclidaifcdcmtifdchdlimqvdclhbsldcliodxmodaidclidaifcdcmtifdchdsicdtmkuiudekp"

# Lấy các ký tự chỉ xuất hiện 1 lần
unique_chars = unique_characters(input_string)

# In ra kết quả
print("Các ký tự chỉ xuất hiện 1 lần:", ''.join(unique_chars))