if __name__ == "__main__":
    import city_table, Keys, GetResponse
else:
    from . import city_table, Keys, GetResponse

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/"
feature = "getVilageFcst"
serviceKey = Keys.serviceKey


def GetWeather(si, gun, dong):
    try:
        nx, ny = city_table.find_coord(si, gun, dong)
        contents = GetResponse.GetResponse(url, feature, serviceKey, nx, ny)
        return contents
    except:
        print("유효하지 않은 주소입니다.")
        raise


if __name__ == "__main__":
    si, gun, dong = input("시 군 구 띄어쓰기로 입력하세요").split()
    fcsts = GetWeather(si, gun, dong)
    print(fcsts.fcst["SKY"])

## 함수 테스트
# test = GetWeather("대전광역시", "유성구", "신성동")
# print(test.fcst_now)

# for fcsts in zip(
#     test.fcst["TMP"], test.fcst["SKY"], test.fcst["WSD"], test.fcst["POP"], test.fcst["REH"]
# ):
#     print("date:", fcsts[0][0], "time:", fcsts[0][1])
#     for fcst in fcsts:
#         print(fcst[2])
