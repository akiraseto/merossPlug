# merossPlug

## Features
MerossのIOT電源タップ(4口+USB モデル番号:mss425f)をコードで制御する

## Requirement

## Installation
```bash
mv config_sample.py config.py 
```

リネームしたconfig.pyに値を設定して下さい。


## Usage


## Note

### 調査
mitmproxyを使いMerossのiOSアプリと電源タップ間にman in the middleしてapiを調べた

```bash
#mitmproxy
pip install mitmproxy

```

### jsonファイル

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

#### 使用例
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
