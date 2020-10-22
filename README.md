# merossPlug

## Features
MerossのIOT電源タップ(4口+USB モデル番号:mss425f)をコードで制御する

## Requirement
- python

```bash
pip install requests

```

- mitmproxy
configのip_address,messageId,sign,timestampの変数を取得するのに必要。

```bash
#mitmproxy
pip install mitmproxy

```


## Installation
```bash
mv config_sample.py config.py 
```

リネームしたconfig.pyに値を設定して下さい。

## Usage

```bash

# 1番口をオン
python main.py 1 on

# 全部をオフ
python main.py 0 off

```

- 第1引数: タップ口番号(1-5, all:0)
- 第2引数: on off 通電のオン・オフ


## Note
mitmproxyを使いMerossのiOSアプリと電源タップ間にman in the middleしてapi,jsonを調査

```json

{
  "header": {
    "from": "http://xxx.xxx.xxx.xxx/config",
    "messageId": "xxxxx",
    "method": "SET",
    "namespace": "Appliance.Control.ToggleX",
    "payloadVersion": 1,
    "sign": "xxxxx",
    "timestamp": 1234567890,
    "triggerSrc": "iOS"
  },
  "payload": {
    "togglex": {
      "channel": 1,
      "onoff": 1
    }
  }
}

```

- channel: タップ口番号、1から昇順。全ては0
- onoff: 1がon,0がoff
- signとtimestampは連動しているっぽい
- messageIdは取得したものを使用
- triggerSrc: 任意の文字列でOKっぽい

triggerSrcと、payload内以外はmitmで取得したものをそのまま使うことで動作する。

## PS
Apple Homeに連動させて、iPhone,AppleWatchを用いて使用している
Apple Homeとの連携には、Homebridgeを使用

```bash
#homebridge
npm i homebridge

```


## Author

- akinko
- akira.seto@gmail.com
- [Qiita](https://qiita.com/akinko)


## License

[MIT license](https://en.wikipedia.org/wiki/MIT_License).
