---
nav_title: KakaoTalk einrichten
article_title: "KakaoTalk einrichten"
description: "Dieser Referenzartikel beschreibt, wie Sie Ihren KakaoTalk-Kanal einrichten, einschließlich der Einrichtung von Nutzer:innen, der Abstimmung von Nutzer-IDs und der Erstellung von Testnutzer:innen."
page_order: 0
alias: /kakaotalk_setup/
channel:
  - KakaoTalk
---

# KakaoTalk einrichten

> Dieser Artikel beschreibt, wie Sie den [KakaoTalk-Messaging-Kanal]({{site.baseurl}}/kakaotalk/) in Braze einrichten, einschließlich der Einrichtung von Nutzer:innen, der Abstimmung von Nutzer-IDs und der Erstellung von KakaoTalk-Testnutzer:innen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Konto bei einem unterstützten KakaoTalk-Partner | Ein Konto bei einem unterstützten KakaoTalk-Partner, [CJ OliveNetworks](https://www.braze.com/partners/solutions-partners/cjolivenetworks/) oder Infobip, ist erforderlich, um den KakaoTalk-Messaging-Kanal zu nutzen. |
| KakaoTalk-Business-Kanal | Ihr KakaoTalk-Konto muss ein KakaoTalk-Business-Kanal sein, um KakaoTalk-Nachrichten über Braze zu senden. Wenn Sie ein Konto erstellen, ist der Standardstatus „Basic". Um Ihr Konto zu einem Business-Kanal zu machen, müssen Sie Ihr Unternehmen verifizieren und die entsprechenden Dokumente bereitstellen. |
| KakaoTalk-Sender-Key | Ein gültiger KakaoTalk-Sender-Key. |
| Kontakt-Telefonnummer | Eine Kontakt-Telefonnummer für die Administration Ihres KakaoTalk-Kanals. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Arten von KakaoTalk-Konten

| Kontotyp | Beschreibung |
| --- | --- |
| Basic-Kanal | Ein Standard-KakaoTalk-Kanal, den jede Organisation einrichten kann. Er ermöglicht Broadcast-Messaging und 1:1-Chat über KakaoTalk. |
| [Business-Kanal](https://www.kakaocorp.com/page/service/service/KakaoTalkChannel) | Ein erweiterter, geschäftlich verifizierter KakaoTalk-Kanal, der einen Antrags- und Verifizierungsprozess erfordert. Er bietet erweiterte Features, wie z. B. {::nomarkdown}<ul><li>Verifiziertes Badge</li><li>Anzeige als empfohlener Kanal</li><li>Unterstützung für Business-Messaging</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Einen Business-Kanal beantragen

Bevor Sie den Antrag starten, sammeln Sie die folgenden Geschäftsdokumente:
- Koreanische Gewerbeanmeldung (Korean Business Registration Certificate)
- Ausweis der Unternehmensvertretung
- Beschäftigungsnachweis
- Branchenspezifische Lizenzen

{% alert important %}
Die Informationen in Ihrem KakaoTalk-Kanal (wie Kanalname, Profilbild und andere) müssen exakt mit den Informationen in Ihren offiziell eingereichten Dokumenten übereinstimmen.
{% endalert %}

Nachdem Sie Ihre Dokumente zusammengestellt haben, folgen Sie diesen Schritten:

1. Melden Sie sich im [KakaoTalk Channel Admin Center](https://center-pf.kakao.com/) an.
2. Wählen Sie den bestehenden KakaoTalk-Kanal aus, den Sie upgraden möchten.
3. Wählen Sie im Abschnitt **Management (관리)** die Option **Business Channel Application (비즈니스 채널 신청)** aus.
4. Wählen Sie den Button **Apply** oder **Request (신청)** aus, um den Prozess zu starten.
5. Geben Sie die erforderlichen Informationen an.
6. Warten Sie auf eine Benachrichtigung mit den Ergebnissen der Überprüfung.

## KakaoTalk integrieren

### 1. Schritt: Den KakaoTalk-Kanal mit Braze verbinden

1. Gehen Sie zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie Ihren KakaoTalk-Anbieter aus.
2. Sammeln Sie die erforderlichen Zugangsdaten für Ihren Anbieter (siehe unten), geben Sie diese auf der Seite **Technologiepartner** ein und speichern Sie sie.
3. Verwenden Sie die neu gespeicherten Zugangsdaten zum Senden.

#### CJ OliveNetworks

Gehen Sie zu Ihrem [Comm.One-Dashboard](https://ums.cjmplace.com/) und sammeln Sie die folgenden Informationen.

| Feld | Ort |
| --- | --- |
| **Comm.One Login ID (로그인 아이디)** | Wählen Sie Ihr Profil aus. |
| **Sender Key (발신프로필 키)** | Gehen Sie zu **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Channel name (카카오톡 채널 프로필명)** | Gehen Sie in Ihrem Comm.One-Dashboard zu **Template Management (템플릿 관리)** > **Sender Profile Management (발신프로필 관리)**. |
| **Sender number (연락처)** | {::nomarkdown}<ol><li>Gehen Sie zu <b>Account Management (계정 관리)</b>, wählen Sie das Menüsymbol und dann <b>View Details (자세히보기)</b> aus.</li><li>Gehen Sie zu <b>Business Detailed Information (업체 상세 정보)</b> > <b>Company Information (기업정보)</b></li></ul>{:/} |
| **Credential (ID) & Password (비밀번호)** | Gehen Sie zum selben Ort wie für die **Sender number (사업자 등록번호)** und dann zu **API** > **Brand Message (브랜드 메시지)**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs local %}
{% tab Comm.One Login ID (로그인 아이디) %}

![Comm.One-Dashboard mit einer zensierten Login-ID.]({% image_buster /assets/img/kakaotalk/comm.one_login_id.png %})

{% endtab %}
{% tab Sender Key (발신프로필 키) %}

![Comm.One-Dashboard mit einem zensierten Sender Key.]({% image_buster /assets/img/kakaotalk/sender_key.png %})

{% endtab %}
{% tab Channel name (카카오톡 채널 프로필명) %}

![Comm.One-Dashboard mit einem zensierten Kanalnamen.]({% image_buster /assets/img/kakaotalk/channel_profile_name.png %})

{% endtab %}
{% tab Credential (ID) & Password (비밀번호) %}

![Comm.One-Dashboard mit einer zensierten Credential-ID und einem zensierten Passwort.]({% image_buster /assets/img/kakaotalk/id_and_password.png %})

{% endtab %}
{% endtabs %}

![Felder auf der Seite „Technologiepartner" für CJ OliveNetworks.]({% image_buster /assets/img/kakaotalk/cj_olivenetworks.png %}){: style="max-width:30%;"}

![Zugangsdaten für einen Braze-KakaoTalk-Kanal.]({% image_buster /assets/img/kakaotalk/cj_credentials.png %})

{% alert note %}
Es können nur die Kanäle registriert werden, die einer einzelnen gemeinsamen ID zugeordnet sind.
{% endalert %}

#### Infobip

Gehen Sie zu Ihrem Infobip-Dashboard und sammeln Sie die folgenden Informationen.

| Feld | Ort |
| --- | --- |
| **API Base URL** | Wählen Sie **Developer Tools** > **API Keys** aus. |
| **API-Schlüssel** | Wählen Sie **Developer Tools** > **API Keys** aus. |
| **Sender name / Sender key** | Wählen Sie **Channels and Numbers** > **Channels** aus und dann den Tab **Absender**. |
| **Sender profile UUID** | Wird direkt von Infobip bereitgestellt. Kontaktieren Sie Infobip, wenn Sie diese Information nicht haben. |
| **Channel name** | Wird direkt von Infobip bereitgestellt. Kontaktieren Sie Infobip, wenn Sie diese Information nicht haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Nutzerprofile einrichten

Nutzerprofile müssen Telefonnummern enthalten, damit ihnen Nachrichten über KakaoTalk gesendet werden können. Telefonnummern werden im Nutzerprofil in dem Format angezeigt, in dem sie bereitgestellt wurden. Im Gegensatz zu SMS oder WhatsApp verwendet KakaoTalk derzeit das Standard-Telefonnummernfeld (und nicht eine Nummer, die in das E.164-Format umgewandelt wurde).

![Nutzerprofil einer Testnutzerin bzw. eines Testnutzers mit einer Telefonnummer in unbearbeitetem Format.]({% image_buster /assets/img/kakaotalk/standard_phone_number.png %}){: style="max-width:50%;"}

### Telefonnummern importieren

Importieren Sie Telefonnummern, indem Sie [eine CSV-Datei hochladen oder die API verwenden]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/), um Nutzer:innen zu erstellen.