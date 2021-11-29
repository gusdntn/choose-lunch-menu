lunchmenu = [' ','1.한식', '2.중식','3.양식']
menu1 = [' ','1.제육 짜글이','2.김밥','3.콩불', '4.돼지국밥']
price1 = [0, 5000, 3000, 8000, 8000]
menu2 = [' ','1.짜장면', '2.짬뽕', '3.탕수육', '4.군만두']
price2 = [0, 5000, 6000, 9000, 4000]
menu3 = [' ','1.스테이크', '2.파스타', '3.샐러드', '4.햄버거']
price3 = [0, 11000, 8000, 6500, 5500]
bill = [0, 50000, 10000, 5000, 1000]

print('고독한 대학생을 위한 점심 메뉴 프로그램입니다.')
print()
select = int(input("한식, 중식, 양식 중 하나를 고르세요.: "))
k = lunchmenu[select]

if k == '1.한식':
    print()
    print('<메뉴>\n', '1.제육 짜글이 5000원\n', '2.김밥 3000원\n', '3.콩불 8000원\n', '4.돼지국밥 8000원\n')
    n = int(input("메뉴를 고르세요.: "))
    print()
    price_sum = price1[n]
    print(menu1[n], price1[n], '원', '합계', price_sum, '원')
    print()

    while n != 0:
        n = int(input(">>> 추가 주문은 음식 번호를, 지불은 0을 누르세요 : "))
        print()

        if n > 0 and n <len(menu1):
            price_sum = price_sum + price1[n]
            print(menu1[n], price1[n], '원', '합계', price_sum, '원')
            print()
        else :
           if n == 0:
             pay = int(input(">>> 현금 결제는 1번, 카드 결제는 2번을 눌러주세요: "))
             print()
             if pay == 1:
              while pay < price_sum:
               n1 = int(input(" >>> 현금을 넣어주세요. "))
               print()
               
               if n1 >= price_sum:
                  print('[총 지불액]: ', n1,'원')
                  print()
                  change = n1 - price_sum
                  print('[거스름돈]: ', change, '원')
                  print()
                  print('>>> 결제가 완료되었습니다.')
                  break
                
               else:
                   print('*돈이 모자랍니다. 다시 넣어주세요.*')
                   print()
                   continue

             else:
                  print(">>> 카드를 넣어주세요.")
                  print()
                  print(">>> 결제가 완료되었습니다.")
                  break
                  

if k == '2.중식':
    print()
    print('<메뉴>\n', '1.짜장면 5000원\n', '2.짬뽕 6000원\n', '3.탕수육 9000원\n', '4.군만두 4000원\n')
    n = int(input("메뉴를 고르세요.: "))
    print()
    price_sum = price2[n] 
    print(menu2[n], price2[n],'원\n','>>> 합계 ', price_sum, '원')
    print()

    while n != 0:
        n = int(input(">>> 추가 주문은 음식 번호를, 지불은 0을 누르세요 : "))
        print()

        if n > 0 and n <len(menu2):
            price_sum = price_sum + price1[n]
            print(menu2[n], price2[n], '원', '합계', price_sum, '원')
            print()
        else :
           if n == 0:
             pay = int(input(">>> 현금 결제는 1번, 카드 결제는 2번을 눌러주세요: "))
             print()
             if pay == 1:
              while pay < price_sum:
               n2 = int(input(" >>> 현금을 넣어주세요. "))
               print()
               
               if n2 >= price_sum:
                  print('[총 지불액]: ', n2,'원')
                  print()
                  change = n2 - price_sum
                  print('[거스름돈]: ', change, '원')
                  print()
                  print('>>> 결제가 완료되었습니다.')
                  break
               else:
                   print('*돈이 모자랍니다. 다시 넣어주세요.*')
                   print()
                   continue

             else:
                  print(">>> 카드를 넣어주세요.")
                  print()
                  print(">>> 결제가 완료되었습니다.")

                  
if k == '3.양식':
    print()
    print('<메뉴>\n', '1.스테이크 11000원\n', '2.파스타 8000원\n', '3.샐러드 6500원\n', '4.햄버거 5500원\n')
    n = int(input("메뉴를 고르세요.: "))
    print()
    price_sum = price3[n] 
    print(menu3[n], price3[n],'원\n','>>> 합계 ', price_sum, '원')
    print()

    while n != 0:
        n = int(input(">>> 추가 주문은 음식 번호를, 지불은 0을 누르세요 : "))
        print()

        if n > 0 and n <len(menu3):
            price_sum = price_sum + price3[n]
            print(menu3[n], price3[n], '원', '합계', price_sum, '원')
            print()
        else :
           if n == 0:
             pay = int(input(">>> 현금 결제는 1번, 카드 결제는 2번을 눌러주세요: "))
             print()
             if pay == 1:
              while pay < price_sum:
               n3 = int(input(" >>> 현금을 넣어주세요. "))
               print()
               
               if n3 >= price_sum:
                  print('[총 지불액]: ', n3,'원')
                  print()
                  change = n3 - price_sum
                  print('[거스름돈]: ', change, '원')
                  print()
                  print('>>> 결제가 완료되었습니다.')
                  break
               else:
                   print('*돈이 모자랍니다. 다시 넣어주세요.*')
                   print()
                   continue

             else:
                  print(">>> 카드를 넣어주세요.")
                  print()
                  print(">>> 결제가 완료되었습니다.")
