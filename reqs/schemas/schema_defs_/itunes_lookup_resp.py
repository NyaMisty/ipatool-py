__all__ = ['iTunesLookupResp']

testin_text = r'''{
  "resultCount": 1,
  "results": [
    {
      "appletvScreenshotUrls": [],
      "screenshotUrls": [
        "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/4e/24/2c/4e242c7d-79ed-601d-39be-f1b5e748a3d9/9d25db85-b88b-4eff-b2a7-be82388b67ec_1_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is3-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/d5/bc/01/d5bc01ff-460f-5235-cf43-da2ed4d03644/1252e8ac-0ae1-455c-a12b-0a16b22d344d_2_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is3-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/57/db/f2/57dbf292-fc33-e1eb-a2fe-24b767630304/e209a06f-21a7-4aba-bbc8-bc93d48569f4_3_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is5-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/57/d2/1a/57d21acc-2a73-646c-be3d-f1c60a019245/8a19d01a-da35-4278-9797-14944f668fdf_4_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/ff/45/11/ff451178-a851-914c-1262-3fc83d063303/9f69be23-92c8-4a99-bf9b-5669cee96072_5_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is5-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/f2/21/5a/f2215a1e-96dc-8404-de87-28b88f2a05ef/e00b4277-b11b-443e-ae13-fa8583aa351c_6_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is3-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/d6/15/9f/d6159fd0-e41e-e298-6452-ae575be4feb1/3e0cef5e-dbc3-493c-a422-136a69901f31_7_iOS_2208x1242_5.5.png/406x228bb.png",
        "https://is4-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/c9/40/51/c9405182-97f1-4b03-1205-71b523a1a794/e4489f02-e26b-4a5a-beac-12117a1867e4_8_iOS_2208x1242_5.5.png/406x228bb.png"
      ],
      "ipadScreenshotUrls": [
        "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/a0/00/44/a000443c-cf41-1835-c851-cf626e8d3b14/f794994d-a9f7-4b6f-a4aa-edf09431c689_1_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/27/97/b1/2797b165-8009-6528-4fb5-7afbfb4c1f63/c0cac512-461e-4be6-b72b-bd55f22b5d26_2_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is4-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/45/42/d4/4542d4dd-4a20-9a9c-5cdc-ddff457bf856/dac48b98-a892-41a3-9a1f-829be0cf96b3_3_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/b9/f8/09/b9f80930-44dc-3092-e7b7-d08b853bdfb7/303d06ce-ead5-414f-ae32-1509eb6189ba_4_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is3-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/fc/76/24/fc76246e-def5-e27a-ec7a-8cc30180f16a/183a4989-44f8-43c7-8565-8d3bd8cf692d_5_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/86/1a/13/861a13e1-a8a4-cc52-b7cf-11ab4ba120f7/90fd6da6-274a-45c3-a5ee-ffa6cb04ac8b_6_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/ef/26/8f/ef268f72-fefc-5f03-de73-6697c1e1fdd9/15683dcd-0a78-48c5-b1e4-8101dc01be25_7_iOS_2732x2048_12.9.png/552x414bb.png",
        "https://is2-ssl.mzstatic.com/image/thumb/PurpleSource114/v4/d8/9a/e2/d89ae2fc-71e2-1430-235d-f9f0ea06fadf/2a1c9d0f-c11f-410f-9674-022d2f225953_8_iOS_2732x2048_12.9.png/552x414bb.png"
      ],
      "artworkUrl60": "https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/18/4c/2d/184c2d46-7900-05ec-103c-158bdc741508/source/60x60bb.jpg",
      "artworkUrl512": "https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/18/4c/2d/184c2d46-7900-05ec-103c-158bdc741508/source/512x512bb.jpg",
      "artworkUrl100": "https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/18/4c/2d/184c2d46-7900-05ec-103c-158bdc741508/source/100x100bb.jpg",
      "artistViewUrl": "https://apps.apple.com/jp/developer/klab-inc/id302647750?uo=4",
      "supportedDevices": [
        "iPhone5s-iPhone5s",
        "iPadAir-iPadAir",
        "iPadAirCellular-iPadAirCellular",
        "iPadMiniRetina-iPadMiniRetina",
        "iPadMiniRetinaCellular-iPadMiniRetinaCellular",
        "iPhone6-iPhone6",
        "iPhone6Plus-iPhone6Plus",
        "iPadAir2-iPadAir2",
        "iPadAir2Cellular-iPadAir2Cellular",
        "iPadMini3-iPadMini3",
        "iPadMini3Cellular-iPadMini3Cellular",
        "iPodTouchSixthGen-iPodTouchSixthGen",
        "iPhone6s-iPhone6s",
        "iPhone6sPlus-iPhone6sPlus",
        "iPadMini4-iPadMini4",
        "iPadMini4Cellular-iPadMini4Cellular",
        "iPadPro-iPadPro",
        "iPadProCellular-iPadProCellular",
        "iPadPro97-iPadPro97",
        "iPadPro97Cellular-iPadPro97Cellular",
        "iPhoneSE-iPhoneSE",
        "iPhone7-iPhone7",
        "iPhone7Plus-iPhone7Plus",
        "iPad611-iPad611",
        "iPad612-iPad612",
        "iPad71-iPad71",
        "iPad72-iPad72",
        "iPad73-iPad73",
        "iPad74-iPad74",
        "iPhone8-iPhone8",
        "iPhone8Plus-iPhone8Plus",
        "iPhoneX-iPhoneX",
        "iPad75-iPad75",
        "iPad76-iPad76",
        "iPhoneXS-iPhoneXS",
        "iPhoneXSMax-iPhoneXSMax",
        "iPhoneXR-iPhoneXR",
        "iPad812-iPad812",
        "iPad834-iPad834",
        "iPad856-iPad856",
        "iPad878-iPad878",
        "iPadMini5-iPadMini5",
        "iPadMini5Cellular-iPadMini5Cellular",
        "iPadAir3-iPadAir3",
        "iPadAir3Cellular-iPadAir3Cellular",
        "iPodTouchSeventhGen-iPodTouchSeventhGen",
        "iPhone11-iPhone11",
        "iPhone11Pro-iPhone11Pro",
        "iPadSeventhGen-iPadSeventhGen",
        "iPadSeventhGenCellular-iPadSeventhGenCellular",
        "iPhone11ProMax-iPhone11ProMax",
        "iPhoneSESecondGen-iPhoneSESecondGen",
        "iPadProSecondGen-iPadProSecondGen",
        "iPadProSecondGenCellular-iPadProSecondGenCellular",
        "iPadProFourthGen-iPadProFourthGen",
        "iPadProFourthGenCellular-iPadProFourthGenCellular",
        "iPhone12Mini-iPhone12Mini",
        "iPhone12-iPhone12",
        "iPhone12Pro-iPhone12Pro",
        "iPhone12ProMax-iPhone12ProMax",
        "iPadAir4-iPadAir4",
        "iPadAir4Cellular-iPadAir4Cellular",
        "iPadEighthGen-iPadEighthGen",
        "iPadEighthGenCellular-iPadEighthGenCellular",
        "iPadProThirdGen-iPadProThirdGen",
        "iPadProThirdGenCellular-iPadProThirdGenCellular",
        "iPadProFifthGen-iPadProFifthGen",
        "iPadProFifthGenCellular-iPadProFifthGenCellular"
      ],
      "advisories": [],
      "isGameCenterEnabled": true,
      "kind": "software",
      "features": [
        "gameCenter",
        "iosUniversal"
      ],
      "minimumOsVersion": "9.0",
      "trackCensoredName": "ラブライブ！スクールアイドルフェスティバルALL STARS",
      "languageCodesISO2A": [
        "JA"
      ],
      "fileSizeBytes": "3091658752",
      "formattedPrice": "無料",
      "contentAdvisoryRating": "4+",
      "averageUserRatingForCurrentVersion": 4.60778,
      "userRatingCountForCurrentVersion": 170241,
      "averageUserRating": 4.60778,
      "trackViewUrl": "https://apps.apple.com/jp/app/%E3%83%A9%E3%83%96%E3%83%A9%E3%82%A4%E3%83%96-%E3%82%B9%E3%82%AF%E3%83%BC%E3%83%AB%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB%E3%83%95%E3%82%A7%E3%82%B9%E3%83%86%E3%82%A3%E3%83%90%E3%83%ABall-stars/id1377018522?uo=4",
      "trackContentRating": "4+",
      "releaseDate": "2019-09-25T07:00:00Z",
      "genreIds": [
        "6014",
        "7011",
        "6016",
        "7002"
      ],
      "primaryGenreName": "Games",
      "trackId": 1377018522,
      "trackName": "ラブライブ！スクールアイドルフェスティバルALL STARS",
      "sellerName": "KLab Inc.",
      "isVppDeviceBasedLicensingEnabled": true,
      "currentVersionReleaseDate": "2021-04-19T06:03:40Z",
      "releaseNotes": "・スクスタビッグライブで、稀にアプリが強制終了してしまう場合がある不具合を修正\n・その他不具合を修正",
      "primaryGenreId": 6014,
      "currency": "JPY",
      "version": "2.3.1",
      "wrapperType": "software",
      "artistId": 302647750,
      "artistName": "KLab Inc.",
      "genres": [
        "ゲーム",
        "ミュージック",
        "エンターテインメント",
        "アドベンチャー"
      ],
      "price": 0,
      "description": "■虹ヶ咲学園スクールアイドル同好会を楽しむならスクスタ！\nニジガクそれぞれのメンバーの楽曲に込められた成長物語\nその全てがスクスタに！\n\nμ's、Aqoursのライブでおなじみのアニメダンスシーンとのシンクロ\n虹ヶ咲学園スク ールアイドル同好会のライブではスクスタに登場するダンスMVシーンがステージパフォーマンスに！\n\nストーリーに織り込まれたライブステージへの道\n\"ストーリー\"で語られる葛藤や成長を通じて夢へと一歩ずつ近づく彼女たちとあなたの物語はそのまま虹 ヶ咲学園スクールアイドル同好会キャスト達の成長の軌跡とリンクしていきます\n\n「あなた」が主人公であるスクスタではそんなストーリーとは別に\nμ's、Aqours、虹ヶ咲学園スクールアイドル同好会のメンバーとの「あなたとだけの物語」 が繰り広げられる “キズナエピソード” も！\n\n■夢のステージをスクールアイドルの一番近くで目指そう！\n目指すのは最高のライブ！\n\nライブの成功のために “合宿”に行ったり練習を通じてスクールアイドル達の個性を伸ばしたり、本番のライブでは彼女たちのパフォーマンスを手伝ったり…\nあなたとの交流やライブを通じて夢のステージを目指し成長していく物語を盛り立てる要素も盛りだくさん！\n\n＜豊富なゲームコンテンツ＞\n■スクールアイドルチャンネル\n・メンバーのチャンネルに加入して「あなた」の応援でメンバーをトップに輝かせよう！\n\n■色んな楽しみ方ができるイベントも開催\n・全国のプレイヤーと協力プレイ！一番多くボルテージを稼いでMVPを目指そう！ “スクスタビッグライブ”\n・様々なステージを戦力を結集させてクリアしよう！あの子もこの子も活躍させたい！総力戦  “ドリームライブパレード”\n\n■オールスターならではの魅力が満載！\n・28人のスクールアイドルが紡ぐオリジナルストーリー\n　毎月配信されるイベントストーリーではμ's、Aqours、ニジガクのメンバーが奮闘!?\n\n・圧巻の3DMVシーン\n　 アニメに登場したあの楽曲のあのシーンももちろん登場！\n　\n・ゲームならではのカスタマイズ要素\n　28人のスクールアイドルからの組み合わせは自由！あなたが選ぶメンバーで自分だけのライブを楽しもう！\n\n・毎日配信される日常の一コマ “毎日劇場”\n　知られざるスクールアイドル達の日常や意外な一面も？！\n　グループや学校の垣根を超えたスクールアイドル達の交流を毎日配信！\n\n■豊富なビジュアルコンテンツ\n　ステージ上のダンスパフォーマンス楽曲衣装だけではないオリジナル衣装も満載\n　かわいいカードイラストはもちろん、3Dステージ衣装も続々追加！\n\nあなたと彼女たちが紡ぐ青春学園ドラマがここに…。\n「みんなで叶える物語」を体感しよう！\n\n■スクフェスIDについて\n本アプリではスクフェスIDと連携することで、ラブライブ！スクールアイドルフェスティバルとも連動して相互にお楽しみいただけます\n\n■利用規約\nhttps://lovelive-as.bushimo.jp/agreement/",
      "bundleId": "com.klab.lovelive.allstars",
      "userRatingCount": 170241
    }
  ]
}'''

schema = {
  "title": "iTunes Lookup",
  "type": "object",
  "properties": {
    "resultCount": {
      "type": "integer"
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "appletvScreenshotUrls": {
            "type": "array",
            "items": {
              "items": {}
            }
          },
          "screenshotUrls": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "ipadScreenshotUrls": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "artworkUrl60": {
            "type": "string"
          },
          "artworkUrl512": {
            "type": "string"
          },
          "artworkUrl100": {
            "type": "string"
          },
          "artistViewUrl": {
            "type": "string"
          },
          "supportedDevices": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "advisories": {
            "type": "array",
            "items": {
              "items": {}
            }
          },
          "isGameCenterEnabled": {
            "type": "boolean"
          },
          "kind": {
            "type": "string"
          },
          "features": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "minimumOsVersion": {
            "type": "string"
          },
          "trackCensoredName": {
            "type": "string"
          },
          "languageCodesISO2A": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "fileSizeBytes": {
            "type": "string"
          },
          "formattedPrice": {
            "type": "string"
          },
          "contentAdvisoryRating": {
            "type": "string"
          },
          "averageUserRatingForCurrentVersion": {
            "type": "number"
          },
          "userRatingCountForCurrentVersion": {
            "type": "integer"
          },
          "averageUserRating": {
            "type": "number"
          },
          "trackViewUrl": {
            "type": "string"
          },
          "trackContentRating": {
            "type": "string"
          },
          "releaseDate": {
            "type": "string"
          },
          "genreIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "primaryGenreName": {
            "type": "string"
          },
          "trackId": {
            "type": "integer"
          },
          "trackName": {
            "type": "string"
          },
          "sellerName": {
            "type": "string"
          },
          "isVppDeviceBasedLicensingEnabled": {
            "type": "boolean"
          },
          "currentVersionReleaseDate": {
            "type": "string"
          },
          "releaseNotes": {
            "type": "string"
          },
          "primaryGenreId": {
            "type": "integer"
          },
          "currency": {
            "type": "string"
          },
          "version": {
            "type": "string"
          },
          "wrapperType": {
            "type": "string"
          },
          "artistId": {
            "type": "integer"
          },
          "artistName": {
            "type": "string"
          },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "price": {
            "type": "number"
          },
          "description": {
            "type": "string"
          },
          "bundleId": {
            "type": "string"
          },
          "userRatingCount": {
            "type": "integer"
          }
        },
        "required": [
          "appletvScreenshotUrls",
          "screenshotUrls",
          "ipadScreenshotUrls",
          "artworkUrl60",
          "artworkUrl512",
          "artworkUrl100",
          "artistViewUrl",
          "supportedDevices",
          "advisories",
          "isGameCenterEnabled",
          "kind",
          "features",
          "minimumOsVersion",
          "trackCensoredName",
          "languageCodesISO2A",
          "fileSizeBytes",
          "formattedPrice",
          "contentAdvisoryRating",
          "averageUserRatingForCurrentVersion",
          "userRatingCountForCurrentVersion",
          "averageUserRating",
          "trackViewUrl",
          "trackContentRating",
          "releaseDate",
          "genreIds",
          "primaryGenreName",
          "trackId",
          "trackName",
          "sellerName",
          "isVppDeviceBasedLicensingEnabled",
          "currentVersionReleaseDate",
          "releaseNotes",
          "primaryGenreId",
          "currency",
          "version",
          "wrapperType",
          "artistId",
          "artistName",
          "genres",
          "price",
          "description",
          "bundleId",
          "userRatingCount"
        ]
      }
    }
  },
  "required": [
    "resultCount",
    "results"
  ]
}

# import python_jsonschema_objects as pjs
# builder = pjs.ObjectBuilder(schema)
# ns = builder.build_classes()
# iTunesLookupResp = ns.ItunesLookup

def gen_schema(generator):
    generator.Generate(schema, "", 'iTunesLookupResp', 'itunes_lookup_resp')