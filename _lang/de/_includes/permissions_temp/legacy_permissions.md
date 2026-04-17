{% alert important %}
Braze führt [detaillierte Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) ein, eine flexiblere Methode zur Verwaltung des Zugriffs der Nutzer:innen. Weitere Informationen zum Migrationsprozess, einschließlich der Zuordnung von bisherigen Berechtigungen zu detaillierten Berechtigungen, finden Sie unter [Migration zu detaillierten Berechtigungen]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

## Erstellen eines Berechtigungssatzes

Mit Berechtigungssätzen können Sie Berechtigungen für bestimmte Themenbereiche oder Aktionen bündeln. Sie können Berechtigungssätze auf Dashboard-Nutzer:innen anwenden, die in verschiedenen Workspaces denselben Zugriff benötigen. Um einen Berechtigungssatz zu erstellen, gehen Sie zu **Einstellungen** > **Berechtigungseinstellungen** und wählen Sie dann **Berechtigungssatz erstellen**. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Berechtigungen|
|-----------|----------------|
|Entwickler:innen|"Zugriff auf Entwicklungskonsole"|
|Marketer|"Zugriff auf Kampagnen, Canvase, Cards, Feature-Flags, Segmente, Mediathek und Präferenzcenter" <br> "Assets der Mediathek verwalten"|
|Nutzerverwaltung|"Dashboard-Nutzer:innen verwalten" <br> "Teams verwalten"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Eine Rolle erstellen

Rollen ermöglichen eine bessere Strukturierung durch die Bündelung Ihrer individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Nutzer:innen zu den richtigen Workspaces hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Rollenname | Workspace | Berechtigungen  
----------- | ----------- | ---------
| Marketer – Modemarken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke {:/} | „Zugriff auf Kampagnen, Canvase, Cards, Feature-Flags, Segmente, Mediathek und Präferenzcenter"<br>„Assets der Mediathek verwalten" |
| Marketer – Hautpflegemarken | {::nomarkdown}[DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | „Zugriff auf Kampagnen, Canvase, Cards, Feature-Flags, Segmente, Mediathek und Präferenzcenter" <br>„Assets der Mediathek verwalten" |
| Nutzerverwaltung – Alle Marken | {::nomarkdown}[DEV] Modemarke, [QA] Modemarke, [PROD] Modemarke, [DEV] Hautpflegemarke, [QA] Hautpflegemarke, [PROD] Hautpflegemarke {:/} | „Dashboard-Nutzer:innen verwalten"<br>„Teams verwalten" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Wie unterscheiden sich Berechtigungssätze und Rollen von Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Hinweise zum Hinzufügen von Nutzerberechtigungen zu Teams

Es kann zu Schwierigkeiten kommen, wenn Sie versuchen, Berechtigungen im Braze-Dashboard zu speichern – insbesondere beim Hinzufügen oder Entfernen von Nutzer:innen aus einem Workspace oder beim Hinzufügen zu einem Team. Der Button **Nutzer:innen speichern/aktualisieren** kann ausgegraut sein, wenn die Berechtigungen für die Nutzer:innen mit denen identisch sind, die sie bereits auf Workspace-Ebene besitzen. Diese Einschränkung besteht, da es keinen Vorteil bietet, ein Team zu haben, wenn alle Nutzer:innen über dieselben Berechtigungen wie der gesamte Workspace verfügen.

Um eine Nutzer:in erfolgreich zu einem Team hinzuzufügen und dabei die gleichen Berechtigungen beizubehalten, weisen Sie keine Berechtigungen auf Workspace-Ebene zu. Weisen Sie Berechtigungen stattdessen ausschließlich auf Team-Ebene zu.

## Eingeschränkte Nutzer:innen

Eingeschränkte Nutzer:innen verfügen über spezifische Berechtigungen, die es ihnen ermöglichen, bestimmte Aspekte des Braze-Dashboards zu verwalten, wobei sie im Vergleich zu Unternehmensadmins und Workspace-Admins Einschränkungen unterliegen.

| Berechtigungen | Eingeschränkte Nutzer:innen können die Berechtigungen anderer eingeschränkter Nutzer:innen bearbeiten, wenn sie die Berechtigung „Dashboard-Nutzer:innen verwalten" aktiviert haben. Sie können auch neue eingeschränkte Nutzer:innen anlegen und deren Berechtigungssätze ändern. Allerdings können sie keine Unternehmensadmin-Konten erstellen oder verwalten. |
| Rollenbeschränkungen | Wenn eine eingeschränkte Nutzer:in über alle Berechtigungen außer „App-Gruppenadmin" verfügt, hat sie dennoch Zugriff auf alle anderen Berechtigungen, die normalerweise einem Workspace-Admin gewährt werden. |
| Sichtbarkeit von Berechtigungen | Wenn für eine eingeschränkte Nutzer:in die Option „Dashboard-Nutzer:innen verwalten" für eine App-Gruppe (z. B. Dev) aktiviert ist, jedoch nicht für eine andere (z. B. Prod), werden die Berechtigungen für die App-Gruppe Prod in ihrem Profil „Nutzer:innen verwalten" nicht angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vergleich eingeschränkter Nutzer:innen

| Eingeschränkter Nutzertyp | Beschreibung |
| --- | --- |
| App-Gruppenadmin | App-Gruppenadmins verfügen über Berechtigungen, die speziell für die Verwaltung von App-Gruppen gelten, jedoch nicht über dieselben Befugnisse wie Unternehmensadmins. Eingeschränkte Nutzer:innen können Berechtigungen ähnlich denen von App-Gruppenadmins erhalten, wenn die erforderlichen Berechtigungen aktiviert sind. |
| Unternehmensadmin | Unternehmensadmins verfügen über umfassendere Berechtigungen, einschließlich der Möglichkeit, Dashboard-Nutzer:innen zu löschen. Sie können jedoch ihr eigenes Konto nicht löschen und müssen sich für diese Aktion an einen anderen Unternehmensadmin wenden. |
| Grundlegende Leseberechtigung | Um auf bestimmte Bereiche des Dashboards zugreifen zu können, wie beispielsweise die Technologie-Partnerseite, benötigen Nutzer:innen eine grundlegende Leseberechtigung. Dazu gehört, dass „Externe Integrationen verwalten" aktiviert ist und Berechtigungen für Kampagnen, Canvase, Cards, Segmente und die Mediathek vorhanden sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Fehler bei eingeschränktem Zugriff

Nutzer:innen können Nachrichten wie „Eingeschränkter Zugriff. Sie verfügen nicht über die erforderlichen Berechtigungen, um auf diese Seite zuzugreifen." erhalten. In solchen Fällen sollte der Kontoadmin prüfen, ob das Problem durch Deaktivieren und erneutes Aktivieren der Berechtigungen der Nutzer:innen behoben werden kann.

{% alert note %}
Es ist nicht möglich, Nutzerberechtigungen von einer Dashboard-Nutzer:in auf eine andere zu übertragen oder zu importieren.
{% endalert %}

## Bearbeiten der Berechtigungen einer Nutzer:in

Um die aktuellen Admin-, Unternehmens- oder Workspace-Berechtigungen einer Nutzer:in zu bearbeiten, gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie den Namen aus.

![Die Seite „Unternehmensnutzer:innen" in Braze mit einer Nutzer:in in den Ergebnissen.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Admins haben Zugriff auf alle Features und können alle Unternehmenseinstellungen ändern. Sie können:

- [Genehmigungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval) ändern
- Andere [Braze-Nutzer:innen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) hinzufügen, bearbeiten, löschen, suspendieren oder die Suspendierung aufheben
- Braze-Nutzer:innen als CSV-Datei exportieren

Um Admin-Rechte zu gewähren oder zu entfernen, wählen Sie **Diese Nutzer:in ist Admin** und dann **Nutzer:in aktualisieren**.

![Die Details der ausgewählten Nutzer:in mit aktiviertem Admin-Kontrollkästchen.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Wenn Sie einer Nutzer:in die Admin-Rechte entziehen, kann sie nicht mehr auf Braze zugreifen, bis Sie ihr mindestens eine Berechtigung [auf Unternehmens- oder Workspace-Ebene]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions) zuweisen.
{% endalert %}

{% endtab %}
{% tab Company %}

### Unternehmen

Um die folgenden Berechtigungen auf Unternehmensebene für eine Nutzer:in zu verwalten, aktivieren oder deaktivieren Sie das Kästchen neben der jeweiligen Berechtigung. Wenn Sie fertig sind, wählen Sie **Nutzer:in aktualisieren**.

|Berechtigungsname|Beschreibung|
|----------|-----------|
|Unternehmenseinstellungen verwalten|Ermöglicht es Nutzer:innen, jede Unternehmenseinstellung zu ändern.|
|Workspaces erstellen und löschen|Ermöglicht es Nutzer:innen, Workspaces zu erstellen und zu löschen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

Sie können einer Nutzer:in unterschiedliche Berechtigungen für jeden Workspace erteilen, dem sie in Braze angehört. Um die Berechtigungen auf Workspace-Ebene zu verwalten, wählen Sie **Workspaces und Berechtigungen auswählen** und wählen dann die Berechtigungen manuell aus oder weisen einen [zuvor erstellten]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set) Berechtigungssatz zu.

Wenn Sie einer Nutzer:in unterschiedliche Berechtigungen für verschiedene Workspaces erteilen möchten, wiederholen Sie diesen Vorgang so oft wie nötig. Eine Beschreibung der einzelnen Berechtigungen finden Sie unter [Liste der Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungen** eine oder mehrere Berechtigungen aus der Dropdown-Liste. Braze erteilt diese Berechtigungen ausschließlich für die von Ihnen ausgewählten Workspaces. Optional können Sie **Admin-Zugriff aktivieren** auswählen, wenn Sie der Nutzer:in stattdessen volle Berechtigungen für diesen Workspace geben möchten.

Wenn Sie fertig sind, wählen Sie **Nutzer:in aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die manuell in Braze ausgewählt werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Wählen Sie unter **Workspaces** einen oder mehrere Workspaces aus der Dropdown-Liste. Wählen Sie dann unter **Berechtigungssätze** einen Berechtigungssatz aus. Braze erteilt diese Berechtigungen ausschließlich für die von Ihnen ausgewählten Workspaces.

Wenn Sie fertig sind, wählen Sie **Nutzer:in aktualisieren**.

![Berechtigungen auf Workspace-Ebene, die über einen Berechtigungssatz in Braze zugewiesen werden.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set_legacy.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Nutzerberechtigungen exportieren

Um eine Liste Ihrer Nutzer:innen und deren Berechtigungen herunterzuladen, gehen Sie zu **Einstellungen** > **Unternehmensnutzer:innen** und wählen Sie dann **Nutzer:innen exportieren**. Eine CSV-Datei wird in Kürze an Ihre E-Mail-Adresse gesendet.

![Die Seite „Unternehmensnutzer:innen" in Braze mit der Option „Nutzer:innen exportieren" im Fokus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste der Berechtigungen

|Ebene|Name|Definition|
|---|---|---|
|Admin|Admin|Ermöglicht Nutzer:innen den Zugriff auf alle verfügbaren Features. Dies ist die Standardeinstellung für alle neuen Nutzer:innen. Sie können die Unternehmenseinstellungen (Unternehmensname und Zeitzone) aktualisieren, was eingeschränkten Nutzer:innen nicht möglich ist.|
|Unternehmen|Workspaces erstellen und löschen|Ermöglicht es Nutzer:innen, Workspaces zu erstellen und zu löschen.|
|Unternehmen|Unternehmenseinstellungen verwalten|Ermöglicht es Nutzer:innen, jede Unternehmenseinstellung zu ändern.|
|Workspace|Zugriff auf Kampagnen, Canvase, Cards, Content-Blöcke, Feature-Flags, Segmente, Mediathek, Standorte, Aktionscodes und Präferenzcenter|Ermöglicht Nutzer:innen die Anzeige von Performance-Metriken für Kampagnen und Canvas, die Erstellung und Duplizierung von Entwürfen für Kampagnen und Canvase, die Bearbeitung von Kampagnen- und Canvas-Entwürfen und -Templates, die Anzeige von Entwürfen für Segmente, Templates und Medien, die Erstellung von Templates, den Upload von Medien, die Erstellung oder Aktualisierung von Aktionscode-Listen, die Anzeige von Engagement-Berichten und die Anzeige globaler Nachrichteneinstellungen im Dashboard. Nutzer:innen mit dieser Berechtigung können jedoch keine bestehenden Live-Inhalte anhalten oder bearbeiten.<br><br> Wenn diese Berechtigung als [Team-Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) konfiguriert ist und Kampagnen oder Canvase im [Engagement-Bericht]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) außerhalb der zugewiesenen Teams einer Nutzer:in liegen oder keinen zugewiesenen Teams angehören, wird der Bericht für die Nutzer:in ausgeblendet.|
|Workspace|Zugriff auf Entwicklungskonsole|Ermöglicht den vollen Zugriff auf die folgenden Einstellungen und Protokolle:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API-Schlüssel</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Interne Gruppen</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Nachrichten-Aktivitätsprotokoll</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event-Benutzerprotokoll</a></li></ul>{:/}|
|Workspace|Kampagnen genehmigen und ablehnen|Ermöglicht es Nutzer:innen, Kampagnen zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt. Diese Einstellung befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Account Manager, wenn Sie Interesse an einer Teilnahme haben.|
|Workspace|Canvase genehmigen und ablehnen|Ermöglicht es Nutzer:innen, Canvase zu genehmigen oder abzulehnen. Der [Genehmigungsworkflow für Canvase]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) muss aktiviert sein, damit diese Berechtigung gilt.|
|Workspace|Currents-Integrationen bearbeiten|Ermöglicht es Nutzer:innen, eine Currents-Verbindung zu ändern, einschließlich der Zugangsdaten. Standardmäßig wird Nutzer:innen, denen die Berechtigung „Externe Integrationen" zugewiesen wurde, auch diese Berechtigung zugewiesen.|
|Workspace|Segmente bearbeiten|Ermöglicht Nutzer:innen das Erstellen und Bearbeiten von Segmenten. Sie können auch ohne diese Berechtigung Kampagnen mit bestehenden Segmenten und Filtern erstellen. Sie benötigen diese Berechtigung, um ein Segment aus Nutzer:innen in einer CSV-Datei zu erstellen oder die Gruppe der Nutzer:innen in der CSV-Datei erneut anzusprechen.|
|Workspace|Nutzerdaten exportieren|Ermöglicht es Nutzer:innen, ihre Nutzerdaten aus Segmenten, Kampagnen und Canvase zu exportieren. Diese Berechtigung umfasst sensible Nutzerdaten wie Namen, E-Mail-Adressen und andere gesammelte personenbezogene Daten (PII). Um CSV-Dateien aus dem Dashboard zu exportieren, benötigen Sie diese Berechtigung sowie die Berechtigung „PII anzeigen".|
|Workspace|Nutzerdaten importieren und aktualisieren|Ermöglicht es Nutzer:innen, CSV- und Update-Dateien von App-Nutzer:innen zu importieren und die Seite Nutzerimport anzuzeigen. Hier können Sie auch den Abo-Status einer Nutzer:in und die Opt-in-/Opt-out-Regeln ihrer Abo-Gruppe bearbeiten.|
|Workspace|Content-Blöcke starten und verwalten|Ermöglicht es Nutzer:innen, [Content-Blöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) zu starten und zu verwalten.|
|Workspace|Präferenzcenter starten|Ermöglicht es Nutzer:innen, [Präferenzcenter]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) zu starten.|
|Workspace|Apps verwalten|Ermöglicht Nutzer:innen die Bearbeitung der **App-Einstellungen**.|
|Workspace|Dashboard-Berechtigung für Katalogverwaltung|Ermöglicht es Nutzer:innen, Kataloge zu erstellen und zu verwalten.|
|Workspace|Dashboard-Nutzer:innen verwalten| Ermöglicht es Nicht-Admins, die Seite **Unternehmensnutzer:innen** anzuzeigen, zu bearbeiten und zu verwalten sowie die Dashboard-Nutzer:innen in ihrem Workspace zu verwalten, indem sie die Berechtigungen aller Nutzer:innen, einschließlich ihrer eigenen, ändern. Nutzer:innen mit dieser Berechtigung können keine Nutzer:innen löschen (nur Admins können Nutzer:innen löschen).<br><br>Dies entspricht der bisherigen Berechtigung `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Workspace|E-Mail-Einstellungen verwalten|Ermöglicht es Nutzer:innen, Änderungen an der E-Mail-Konfiguration zu speichern (**Einstellungen** > **E-Mail-Einstellungen**).|
|Workspace|Events, Attribute und Käufe verwalten|Ermöglicht es Nutzer:innen, angepasste Attribute zu bearbeiten (Nutzer:innen ohne diese Berechtigung können angepasste Attribute weiterhin anzeigen), Eigenschaften von angepassten Events zu bearbeiten und anzuzeigen und Eigenschaften von Produkten unter **Dateneinstellungen** zu bearbeiten und anzuzeigen.|
|Workspace|Externe Integrationen verwalten|Ermöglicht den Zugriff auf alle Tabs unter **Technologiepartner**, die Möglichkeit, Braze mit anderen Plattformen zu synchronisieren, und den Zugriff auf die Verwaltung der [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Workspace|Feature-Flags verwalten|Ermöglicht es Nutzer:innen, [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/) zu erstellen oder zu bearbeiten.|
|Workspace|Assets der Mediathek verwalten|Ermöglicht Nutzer:innen das Hinzufügen, Bearbeiten und Löschen von Mediathek-Assets.|
|Workspace|Abo-Gruppen verwalten|Ermöglicht es Nutzer:innen, Abo-Gruppen zu erstellen und zu verwalten.|
|Workspace|Tags verwalten|Ermöglicht Nutzer:innen das Bearbeiten oder Löschen von Tags (unter **Tag-Verwaltung**). Sie benötigen diese Berechtigung nicht, um Tags zu Kampagnen oder Segmenten hinzuzufügen.|
|Workspace|Teams verwalten|Ermöglicht Nutzer:innen die Verwaltung **interner Teams**. Ob Sie diese Berechtigung auswählen können, hängt von Ihrem Vertrag mit Braze ab.<br><br>Dies entspricht der bisherigen Berechtigung `MANAGE_TERRITORIES`.|
|Workspace|Transformationen verwalten|Ermöglicht Nutzer:innen das Erstellen und Verwalten von Datentransformationen.|
|Workspace|Kampagnen und Canvase senden|Ermöglicht es Nutzer:innen, Kampagnen und Canvase zu bearbeiten, zu archivieren und zu stoppen, Kampagnen zu erstellen und Canvase zu starten.|
|Workspace|Abrechnungsdetails anzeigen|Ermöglicht es Nutzer:innen, Abos und Rechnungen einzusehen.|
|Workspace|Currents-Integration anzeigen|Ermöglicht Nutzer:innen die Anzeige aller Informationen über eine Currents-Verbindung, mit Ausnahme der Zugangsdaten. Standardmäßig erhalten Nutzer:innen, denen die Berechtigung „Zugriff auf Kampagnen, Canvase, Cards, Content-Blöcke, Feature-Flags, Segmente, Mediathek, Standorte, Aktionscodes und Präferenzcenter" zugewiesen wurde, auch diese Berechtigung.|
|Workspace|Als PII gekennzeichnete angepasste Attribute anzeigen|Ermöglicht es Nutzer:innen, die keine Admins sind, angepasste Attribute anzuzeigen, die sensible Informationen enthalten und als personenbezogene Daten (PII) gekennzeichnet sind.|
|Workspace|PII anzeigen|Ermöglicht Nutzer:innen die Anzeige von Feldern mit personenbezogenen Daten (PII), wie von Ihrem Unternehmen im Dashboard definiert. Nutzer:innen können PII-Felder auch im Tab **Vorschau als Nutzer:in** der Nachrichtenvorschau sehen.<br><br>Sie benötigen diese Berechtigung, um den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/) zu verwenden, da er direkten Zugriff auf einige Kundendaten ermöglicht. Um CSV-Dateien aus dem Dashboard zu exportieren, benötigen Nutzer:innen sowohl diese Berechtigung als auch die Berechtigung „Nutzerdaten exportieren".|
|Workspace|Nutzerprofile PII-konform anzeigen|Ermöglicht Nutzer:innen die Anzeige von Nutzerprofilen, die Felder enthalten, die Ihr Unternehmen als personenbezogene Daten (PII) definiert hat, wobei die PII-Felder jedoch unkenntlich gemacht werden.<br><br>Sie benötigen diese Berechtigung, um die Nutzersuche zu verwenden.|
|Workspace|Transformationen anzeigen|Ermöglicht es Nutzer:innen, [Braze-Datentransformationen]({{site.baseurl}}/user_guide/data/data_transformation/overview/) anzuzeigen.|
|Workspace|Nutzungsdaten anzeigen|Ermöglicht Nutzer:innen die Anzeige der App-Nutzung, einschließlich der Dashboards für die Kanal-Performance.|
|Workspace|Doppelte Nutzer:innen zusammenführen|Ermöglicht es Nutzer:innen, doppelte Nutzerprofile zusammenzuführen.|
|Workspace|Vorschau doppelter Nutzer:innen anzeigen|Ermöglicht Nutzer:innen eine Vorschau, welche Nutzerprofile dupliziert sind.|
|Workspace|Canvas-Templates erstellen und bearbeiten|Ermöglicht es Nutzer:innen, Canvas-Templates zu erstellen und zu bearbeiten.|
|Workspace|Canvas-Templates anzeigen|Ermöglicht Nutzer:innen die Anzeige von Canvas-Templates.|
|Workspace|Canvas-Templates archivieren|Ermöglicht es Nutzer:innen, Canvas-Templates zu archivieren.|
|Workspace|Eigenschaftssegmentierung für angepasste Events verwalten|Ermöglicht es Nutzer:innen, Segmente auf der Grundlage von Häufigkeit und Aktualität von Event-Eigenschaften zu erstellen.|
|Workspace|Landing-Pages veröffentlichen|Ermöglicht es Nutzer:innen, [Landing-Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/) zu veröffentlichen.|
|Workspace|Entwürfe für Landing-Pages erstellen|Ermöglicht es Nutzer:innen, Entwürfe für Landing-Pages zu erstellen und zu speichern.|
|Workspace|Zugriff auf Landing-Pages|Ermöglicht Nutzer:innen den Zugriff auf die Seite **Landing-Pages**.|
|Workspace|Landing-Page-Templates erstellen und bearbeiten|Ermöglicht es Nutzer:innen, Landing-Page-Templates zu erstellen und zu bearbeiten.|
|Workspace|Landing-Page-Templates anzeigen|Ermöglicht Nutzer:innen die Anzeige von Landing-Page-Templates.|
|Workspace|Landing-Page-Templates archivieren|Ermöglicht es Nutzer:innen, Landing-Page-Templates zu archivieren.|
|Workspace|Angepasste KI-Agenten anzeigen|Ermöglicht es Nutzer:innen, [angepasste KI-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/) anzuzeigen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten erstellen|Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu erstellen. Dieses Feature befindet sich derzeit in der Beta-Phase.|
|Workspace|Angepasste KI-Agenten bearbeiten|Ermöglicht es Nutzer:innen, angepasste KI-Agenten zu bearbeiten. Dieses Feature befindet sich derzeit in der Beta-Phase.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }