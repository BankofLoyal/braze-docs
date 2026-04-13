---
nav_title: "POST:APIトリガーによる配信でキャンペーンを送る"
article_title: "POST:API トリガー配信でキャンペーンを送信する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、API トリガー配信を使用したキャンペーンの送信 Braze エンドポイントの詳細について説明します。"

---
{% api %}
# API トリガー配信を使用したキャンペーンメッセージの送信
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> このエンドポイントを使用して、API トリガー配信により、指定したユーザーに即時の1回限りのメッセージを送信します。

API トリガー配信を使用すると、メッセージのコンテンツを Braze ダッシュボード内に保存しながら、メッセージの送信タイミングと送信先を API を使用して指定できます。

Segment をターゲットにしている場合、リクエストの記録は[開発者コンソール](https://dashboard.braze.com/app_settings/developer_console/activitylog/)に保存されます。このエンドポイントを使用してメッセージを送信するには、[API トリガーキャンペーン]({{site.baseurl}}/api/api_campaigns/)を構築する際に作成した[キャンペーン ID](https://www.braze.com/docs/api/identifier_types/) が必要です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.send` 権限を持つ API キーを生成する必要があります。

## レート制限

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## リクエストパラメーター

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|文字列|[キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`send_id`| オプション | 文字列 | [送信識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
|`trigger_properties`| オプション | オブジェクト | [トリガープロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object/)を参照してください。パーソナライゼーションのキーと値のペアは、このリクエストの全ユーザーに適用されます。 |
|`broadcast`| オプション | ブール値 | Braze ダッシュボードでキャンペーンのターゲットオーディエンスとして設定された Segment 全体にメッセージを送信する場合は、`broadcast` を true に設定する必要があります。このパラメーターのデフォルトは false です（2017年8月31日現在）。<br><br> `broadcast` が true に設定されている場合、`recipients` リストを含めることはできません。ただし、`broadcast: true` を設定する際は注意が必要です。意図せずにこのフラグを設定すると、想定よりも大きなオーディエンスにメッセージが送信される可能性があります。 |
|`audience`| オプション | 接続オーディエンスオブジェクト| [接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)を参照してください。`audience` を含めると、メッセージはカスタム属性やサブスクリプションステータスなど、定義されたフィルターに一致するユーザーにのみ送信されます。 |
|`recipients`| オプション | 配列 | [受信者オブジェクト]({{site.baseurl}}/api/objects_filters/recipient_object/)を参照してください。<br><br>`send_to_existing_only` が `false` の場合、属性オブジェクトを含める必要があります。<br><br>`recipients` が指定されず、`broadcast` が true に設定されている場合、メッセージは Braze ダッシュボードでキャンペーンのターゲットオーディエンスとして設定された Segment 全体に送信されます。<br><br> `email` が識別子の場合、受信者オブジェクトに [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) を含める必要があります。 |
|`attachments`| オプション | 配列 | `broadcast` が true に設定されている場合、`attachments` リストを含めることはできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- 受信者配列には最大50個のオブジェクトを含めることができ、各オブジェクトには単一のユーザー識別子（`external_user_id`、`user_alias`、または `email`）とオプションの `trigger_properties` オブジェクトが含まれます。
- `send_to_existing_only` が `true`（デフォルト）の場合、Braze は既存ユーザーにのみメッセージを送信します。受信者オブジェクト内の識別子（`external_user_id`、`user_alias`、または `email`）が既存のユーザーと一致しない場合、API は `dispatch_id` を含む `201` 成功応答を返しますが、送信は内部的にキャンセルされ、メッセージは配信されません。`external_user_id` の場合、結果は `Unknown External User ID` として記録され、Currents イベントは生成されません。`false` に設定し、属性オブジェクトが提供された場合、Braze はユーザーが存在しない場合に新規ユーザーを作成します。なお、`send_to_existing_only` を `false` に設定することはユーザーエイリアスではサポートされていません&#8212;このエンドポイントを通じてエイリアスのみの新規ユーザーを作成することはできません。エイリアスのみのユーザーに送信するには、そのユーザーが既に Braze に存在している必要があります。

{% alert important %}
`dispatch_id` を含む `201` 応答は、Braze がリクエストを受け付けたことを確認するものであり、メッセージの配信を保証するものではありません。ユーザーが見つからない場合、配信停止している場合、またはそのチャネルの有効な連絡先アドレスを持っていない場合、配信は失敗する可能性があります。
{% endalert %}

ユーザーのサブスクリプショングループのステータスは、`attributes` オブジェクト内に `subscription_groups` パラメーターを含めることで更新できます。詳細については、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)を参照してください。

{% alert note %}
このエンドポイントでは `segment_id` パラメーターはサポートされていません。Segment をターゲットにするには、Braze ダッシュボードのキャンペーンのターゲットオーディエンス設定でセグメントを設定し、`"broadcast": true` を使用するか、[接続オーディエンス]({{site.baseurl}}/api/objects_filters/connected_audience/)フィルターで `audience` パラメーターを使用してください。
{% endalert %}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## 応答の詳細

メッセージ送信エンドポイントの応答には、メッセージのディスパッチを参照するための `dispatch_id` が含まれます。`dispatch_id` はメッセージディスパッチの ID で、Braze から送信される各送信に固有の ID です。このエンドポイントを使用すると、バッチ処理されたユーザーセット全体に対して単一の `dispatch_id` を受け取ります。`dispatch_id` の詳細については、[ディスパッチ ID の動作]({{site.baseurl}}/help/help_articles/data/dispatch_id/)に関するドキュメントを参照してください。

リクエストで致命的なエラーが発生した場合のエラーコードと説明については、[エラーとレスポンス]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

## キャンペーンの属性オブジェクト

Braze には `attributes` というメッセージングオブジェクトがあり、API トリガーキャンペーンを送信する前に、ユーザーの属性や値を追加・作成・更新できます。この API 呼び出しとして `campaign/trigger/send` エンドポイントを使用すると、キャンペーンを処理して送信する前にユーザー属性オブジェクトが処理されます。これにより、[競合]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/)による問題が発生するリスクを最小限に抑えることができます。

{% alert tip %}
このエンドポイントのキャンバスバージョンをお探しですか？[API トリガー配信を使用したキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint)をご確認ください。
{% endalert %}

{% endapi %}