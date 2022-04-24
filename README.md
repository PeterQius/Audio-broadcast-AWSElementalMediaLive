# Audio-broadcast-AWSElementalMediaLive

## 背景信息
AWS Elemental Medialive 是一个广播级的直播服务，它可以为广播电视和互联网多屏设备，创建高质量的视频直播通道。但除了视频外，纯音频的直播需求也越来越多。有自己制作内容后，进行直播推送的场景。也有转推其他源，进行聚合直播的场景，这里主要对第二种情况进行探索。

## AWS与基于开源搭建的平台对比
![image](https://user-images.githubusercontent.com/19642366/164975044-b658bab5-f763-4c99-9228-e787a2fb2e78.png)

#### 方案特点

* 弱化接入端功能，避免过多业务依赖单一组件。不仅减小了系统的容错性和扩展性，也增加了接入端的开发量。
* 接入端只提供单一转流功能，在出现源端或接入端故障时，可以快速切换，而不用考虑系统部署等工作。
* 提供单双通道能力，可以根据业务需求随时调整。每通道提供独立的endpoint（IP）并保障其可用性，不会由于流媒体服务故障，引起配置的变更。
* MediaLive提供的托管流媒体服务端，无任何流媒体服务端开发量（仅需集成API或SDK），并由AWS保障其可靠性和可用性。
* MediaLive可随时启停，不用频繁配置流媒体服务，可随时扩缩，也可以逐步上线，成本和管理可控。

#### 代码部署
1、创建输入  
createinput.py：创建RTP输入

2、创建并启动频道  
create&start channel.py：通过参数或模版创建频道，并且启动频道。并将流保存到S3，同时通过CDN进行分发。

3、流监测  
Detectflow.py：在对大量来源的音频流进行转播的时候，会发现格式、码流等信息各式各样。这里通过FFprobe对每个流进行检测，对需要的流进行转码等操作。

4、删除流  
delchannel&input.py：音频聚合中通常会出现流地址变换，或者流异常等情况。通过删除和重建频道，比较方便的解决业务调整和成本的问题。
