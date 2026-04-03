---
nav_title: KakaoTalk のセットアップ
article_title: "KakaoTalk のセットアップ"
description: "このリファレンス記事では、ユーザーのセットアップ、ユーザー ID の照合、テストユーザーの作成など、KakaoTalk チャネルのセットアップ方法について説明します。"
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalk のセットアップ

> この記事では、Braze で [KakaoTalk メッセージングチャネル]({{site.baseurl}}/kakaotalk/)をセットアップする方法について説明します。ユーザーのセットアップ、ユーザー ID の照合、KakaoTalk テストユーザーの作成方法も含まれます。

## 前提条件

| 要件 | 説明 |
| --- | --- |
| サポートされている KakaoTalk パートナーのアカウント | KakaoTalk メッセージングチャネルを使用するには、サポートされている KakaoTalk パートナー（[CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) または Infobip）のアカウントが必要です。 |
| KakaoTalk ビジネスチャネル | Braze を通じて KakaoTalk メッセージを送信するには、KakaoTalk アカウントが KakaoTalk ビジネスチャネルである必要があります。アカウントを作成すると、デフォルトのステータスはベーシックになります。アカウントをビジネスチャネルにするには、ビジネスの認証を行い、関連する書類を提出する必要があります。 |
| KakaoTalk 発信キー | 有効な KakaoTalk 発信キーが必要です。 |
| 連絡先電話番号 | KakaoTalk チャネルの管理者の連絡先電話番号が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### KakaoTalk アカウントの種類

| アカウントの種類 | 説明 |
| --- | --- |
| ベーシックチャネル | どの組織でもセットアップできる標準の KakaoTalk チャネルです。KakaoTalk を通じたブロードキャストメッセージングと1:1チャットが可能です。 |
| [ビジネスチャネル](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | アップグレードされたビジネス認証済みの KakaoTalk チャネルで、申請と認証プロセスが必要です。以下のような拡張機能を提供します。{::nomarkdown}<ul><li>認証バッジ</li><li>おすすめチャネルとしての表示</li><li>ビジネスメッセージングのサポート</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ビジネスチャネルの申請

申請を開始する前に、以下のビジネス関連書類を準備してください。
- 韓国事業者登録証
- 事業者代表者の身分証明書
- 在職証明書
- 業種別許認可証

{% alert important %}
KakaoTalk チャネルの情報（チャネル名、プロフィール画像など）は、公式に提出した書類の情報と正確に一致する必要があります。
{% endalert %}

書類を準備したら、以下のステップに従ってください。

1. [KakaoTalk チャネル管理センター](https://center-pf.kakao.com/)にログインします。
2. アップグレードしたい既存の KakaoTalk チャネルを選択します。
3. **Management (관리)** セクションで、**Business Channel Application (비즈니스 채널 신청)** のオプションを選択します。
4. **Apply** または **Request button (신청)** を選択してプロセスを開始します。
5. 必要な情報を入力します。
6. 審査結果の通知を待ちます。

## KakaoTalk の統合

### ステップ 1: KakaoTalk チャネルを Braze に接続する

1. **パートナー連携** > **テクノロジーパートナー**に移動し、KakaoTalk プロバイダーを選択します。
2. プロバイダーに必要な認証情報を収集し（以下を参照）、**テクノロジーパートナー**ページに入力して保存します。
3. 新しく保存した認証情報を使用して送信します。

#### CJ OliveNetworks

[Comm.One ダッシュボード](https://ums.cjmplace.com/)にアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | プロファイルを選択します。 |
| **Sender Key (발신프로필 키)** | **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)** に移動します。 |
| **Channel name (카카오톡 채널 프로필명)** | Comm.One ダッシュボードで、**Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)** に移動します。 |
| **Sender number (연락처)** | {::nomarkdown}<ol><li><b>Account Management (계정 관리)</b> に移動し、メニューアイコンを選択してから <b>View Details (자세히보기)</b> を選択します。</li><li><b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b> に移動します。</li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | **Sender number (사업자 등록번호)** と同じ場所に移動し、**API** > **Brand Message (브랜드 메시지)** に移動します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![マスクされたログイン ID が表示されている Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![マスクされた発信キーが表示されている Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![マスクされたチャネル名が表示されている Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![マスクされた認証情報 ID とパスワードが表示されている Comm.One ダッシュボード。]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![CJ OliveNetworks のテクノロジーパートナーページのフィールド。]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Braze KakaoTalk チャネルの認証情報。]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
単一の共通 ID にマッピングされたチャネルのみ登録できます。
{% endalert %}

#### Infobip

Infobip ダッシュボードにアクセスし、以下の情報を収集します。

| フィールド | 場所 |
| --- | --- |
| **API Base URL** | **Developer Tools** > **API Keys** を選択します。 |
| **API キー** | **Developer Tools** > **API Keys** を選択します。 |
| **Sender name / Sender key** | **Channels and Numbers** > **Channels** を選択し、**Senders** タブを選択します。 |
| **Sender profile UUID** | Infobip から直接提供されます。この情報がない場合は、Infobip にお問い合わせください。 |
| **Channel name** | Infobip から直接提供されます。この情報がない場合は、Infobip にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユーザープロファイルの設定

KakaoTalk を通じてメッセージを送信するには、ユーザープロファイルに電話番号が必要です。電話番号はユーザープロファイルに表示され、提供された形式のまま表示されます。現在、SMS や WhatsApp とは異なり、KakaoTalk は標準の電話番号フィールドを使用します（E.164 形式に変換された番号ではありません）。

![編集されていない形式の電話番号を持つテストユーザーのユーザープロファイル。]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### 電話番号のインポート

[CSV のアップロードまたは API の使用]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/)により電話番号をインポートしてユーザーを作成します。