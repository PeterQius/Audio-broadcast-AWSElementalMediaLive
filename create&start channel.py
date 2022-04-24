import boto3
import json
import time

client = boto3.client('medialive')

response = client.create_channel(
    ChannelClass='SINGLE_PIPELINE',
    Destinations=[
        {
            'Id': 'test555',
            'MediaPackageSettings': [],
            'Settings': [
                {
                    'Url': 's3ssl://livedemo2020/stream1/main'
                },
            ]
        },
    ],
    InputAttachments=[
        {
            'InputAttachmentName': 'test111',
            'InputId': '70241',
            'InputSettings': {
                'DeblockFilter': 'DISABLED',
                'DenoiseFilter': 'DISABLED',
                'FilterStrength': 1,
                'InputFilter': 'AUTO',
                'Smpte2038DataPreference': 'IGNORE',
                'SourceEndBehavior': 'CONTINUE',
                'AudioSelectors': [],
                'CaptionSelectors': [],
            }
        },
    ],
    EncoderSettings={
        'AudioDescriptions': [
            {
                'Name': 'audio_00001',
                'AudioSelectorName': '0',
                'AudioTypeControl': 'FOLLOW_INPUT',
                'LanguageCodeControl': 'FOLLOW_INPUT',
                'CodecSettings': {
                    'AacSettings': {
                        'Bitrate': 16000,
                        'CodingMode': 'CODING_MODE_2_0',
                        'InputType': 'NORMAL',
                        'Profile': 'LC',
                        'RateControlMode': 'CBR',
                        'RawFormat': 'NONE',
                        'SampleRate': 8000,
                        'Spec': 'MPEG4',
                    }, 
                },
            },
        ],
        'CaptionDescriptions': [],
        'OutputGroups': [
            {
                'OutputGroupSettings': {
                    'HlsGroupSettings': {
                        'AdMarkers': [],
                        'CaptionLanguageMappings': [],
                        'CaptionLanguageSetting': 'OMIT',
                        'ClientCache': 'ENABLED',
                        'CodecSpecification': 'RFC_4281',
                        'Destination': {
                            'DestinationRefId': 'test555'
                        },
                        'DirectoryStructure': 'SINGLE_DIRECTORY',
                        'DiscontinuityTags': 'INSERT',
                        'HlsId3SegmentTagging': 'DISABLED',
                        'IFrameOnlyPlaylists': 'DISABLED',
                        'IncompleteSegmentBehavior': 'AUTO',
                        'IndexNSegments': 10,
                        'InputLossAction': 'EMIT_OUTPUT',
                        'IvInManifest': 'INCLUDE',
                        'IvSource': 'FOLLOWS_SEGMENT_NUMBER',
                        'KeepSegments': 21,
                        'ManifestCompression': 'NONE',
                        'ManifestDurationFormat': 'FLOATING_POINT',
                        'Mode': 'LIVE',
                        'OutputSelection': 'MANIFESTS_AND_SEGMENTS',
                        'ProgramDateTime': 'EXCLUDE',
                        'ProgramDateTimePeriod': 600,
                        'RedundantManifest': 'DISABLED',
                        'SegmentLength': 10,
                        'SegmentationMode': 'USE_SEGMENT_DURATION',
                        'SegmentsPerSubdirectory': 10000,
                        'StreamInfResolution': 'INCLUDE',
                        'TimedMetadataId3Frame': 'PRIV',
                        'TimedMetadataId3Period': 10,
                        'TsFileMode': 'SEGMENTED_FILES'
                    },
                },
                'Outputs': [
                    {
                        'OutputSettings': {
                            'HlsOutputSettings': {
                                'H265PackagingType': 'HVC1',
                                'HlsSettings': {
                                    'AudioOnlyHlsSettings': {
                                        'AudioGroupId': 'program_audio',
                                        'AudioTrackType': 'AUDIO_ONLY_VARIANT_STREAM',
                                        'SegmentType': 'AAC'
                                    },
                                },
                                'NameModifier': '_1',
                            },
                        },
                        'AudioDescriptionNames': [
                            'audio_00001',
                        ],
                        'CaptionDescriptionNames': [],
                    },
                ]
            },
        ],
        'TimecodeConfig': {
            'Source': 'EMBEDDED',
        },
        'VideoDescriptions': []
    },

    InputSpecification={
        'Codec': 'AVC',
        'MaximumBitrate': 'MAX_10_MBPS',
        'Resolution': 'SD'
    },
    LogLevel='DISABLED',
    Name='test111',
    RoleArn='arn:aws:iam::814424992012:role/MediaLiveAccessRole',
    Tags={}
)

time.sleep(3)

json_res=json.dumps(response)
res=json.loads(json_res)
arn=res["Channel"]["Arn"]
cid=arn.split(':')[-1]
print(cid)
response = client.start_channel(
    ChannelId=cid
)