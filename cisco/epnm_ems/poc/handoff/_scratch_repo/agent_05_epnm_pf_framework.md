# Agent 05 — EPNM `pf-framework` Tree Report Extraction

Source: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EPNM/tree-reports/pf-framework_tree_report.md` (10,160 lines)

Repo: `pf-framework` — 8,518 text files, 1,427 directories, 1,354,236 raw lines, 566 skipped binaries, 1,354 skipped ignored-extension files. Per the tree report header this is `/Users/cmoore/Documents/programming/EPNM/core-framework/pf-framework`.

**Critical finding up front.** The name "pf-framework" (Prime Framework) does not cleanly match the "PI framework" concept from the transcripts. Most of this repo is **server-side provisioning content** (demo/, discovery/, driver/, multivendorsupport/, lib/, pf-framework-techpack/) with `.xde`, `.xjs`, `.vtl`, `.xep`, `.par`, `.xft`, packageDescriptor.xml files — i.e., the XDE/XMP provisioning engine. The **UI framework layer** that underpins EPNM screens lives entirely within one subtree: `ui/`. Specifically the Dojo/Dijit stack plus Cisco's custom "Prime XWT" widget library is under `ui/core/ui_components/lib/`. That is the relevant surface for the Inventory + Fault classic-view rebuild.

## 1. Repo Shape at a Glance

Top-level directories (from tree root):

- `build/` — build scripts, properties, ivy/maven settings (`build-ui.xml`, `build-macros.xml`, `build.properties`, `ivysettings.xml`, `mvn-settings.xml`).
- `demo/` — E-LINE / EPL demo provisioning content (`.xde` flows, `.vtl` Velocity templates, `.rules` Drools, JSON layouts). Not UI framework.
- `discovery/` — `resourcepool/`, `resourcepool-ice-ext/` Java modules for resource-pool discovery.
- `doc/` — empty doc/images folder.
- `driver/` — `ProvDriverWrapper/`, `ProvisioningDriver/`, `order-xml-generator/`, `order-xml-generator-xde/`, `provisioning-service/`, `xmp-pp-helper/`, `xmp-pp-helper-xde/`, `xmp_device_package_test/`. Backend provisioning pipeline.
- `lib/build/` — shared build libs.
- `multivendorsupport/` — `AlcatelSamBootstrap/`, `AlcatelSamUtilities/`, large `mdfdata.xml` (5,792 lines).
- `pf-framework-techpack/` — tech-pack packaging.
- `ui/` — **this is the UI framework.** Three children: `apps/`, `build/`, `core/`, plus `provisioning/`.
- `pom.xml` at root (46 lines).

The tree makes clear: framework/Dojo code lives in `ui/core/ui_components/lib/`; example apps live in `ui/apps/`; server-side extension points for the UI controller live in `ui/core/ProvisioningUIController/` and `ui/core/UI_Controller_Examples/`; UI service/runtime/designer live under `ui/provisioning/UserInterfaceServer/` and `ui/core/ui_designer/`, `ui/core/ui_xde_client/`.

## 2. Widget Library Organization

Custom Dijit widgets and templates live under `ui/core/ui_components/lib/`. The subtree breakdown (representative paths, all verbatim):

- `ui/core/ui_components/lib/dijit/` — stock Dojo Dijit at framework version.
  - `dijit/form/` (TextBox.js, ValidationTextBox.js, FilteringSelect.js, Select.js, NumberTextBox.js, DateTextBox.js, TimeTextBox.js, _FormWidget.js, _FormValueWidget.js, etc.) — 60+ widgets plus `templates/*.html` (Button.html, ValidationTextBox.html, etc.).
  - `dijit/layout/` — AccordionContainer.js, BorderContainer.js, ContentPane.js, StackContainer.js, TabContainer.js, LayoutContainer.js, SplitContainer.js, ScrollingTabController.js, `_LayoutWidget.js`, `_TabContainerBase.js`, `utils.js`, plus `templates/TabContainer.html` etc.
  - `dijit/tree/` — TreeStoreModel.js, ObjectStoreModel.js, ForestStoreModel.js, dndSource.js.
  - `dijit/_editor/` — RichText plus plugins (FullScreen, Print, LinkDialog, etc.).
  - Root Dijit classes: `_WidgetBase.js` (1196 lines), `_Widget.js`, `_TemplatedMixin.js`, `_WidgetsInTemplateMixin.js`, `_Container.js`, `_Contained.js`, `Dialog.js`, `Menu.js`, `Tree.js` (1807 lines), `Tooltip.js`, `TitlePane.js`, `ProgressBar.js`, `Toolbar.js`, `Calendar.js`, `WidgetSet.js`, `registry.js`.

- `ui/core/ui_components/lib/dojo/` — stock Dojo core. `dojo/topic.js` (38 lines), `dojo/_base/*`, `dojo/cldr/`, `dojo/data/`, `dojo/store/`, `dojo/parser.js`, `dojo/request/*`, etc.

- `ui/core/ui_components/lib/dojox/` — Dojo extensions. Grid subtree described in §5. Charting, layout, widget, form, mobile, etc.

- `ui/core/ui_components/lib/xwt/` — **Cisco Prime XWT widget library.** Namespace for all custom Prime widgets. This is the "EPNM look-and-feel" widget set. Key subtrees:
  - `xwt/widget/form/` — custom form widgets that wrap/replace Dijit: ValidationTextBox (at `xwt/widget/notification/ValidationTextBox.js`), ComboBox.js, FilteringSelect.js, DateField.js, DateTimePicker.js, DateTimeRangePicker.js, DropDown.js, IPAddress.js, IPv4TextBox.js, IPv6Address.js, IPv6AddressWithMask.js, UnifiedIPAddress.js, MacTextBox.js, NumberSpinner.js, NumberTextBox.js, PasswordTextBox.js, TextBoxHint.js, TextButton.js, IconButton.js, IconDropDownButton.js, MenuButton.js, CheckBoxGroup.js, CheckedMultiSelect.js, RadioButtonGroup.js, Rating.js, HorizontalSlider.js, VerticalSlider.js, HorizontalRangeSlider.js, VerticalRangeSlider.js, QuickViewHint.js, MultipleFileUpload.js, ListBox.js, GroupBox.js, ToggleButtonGroup.js, ToggleLink.js, Label.js, AnchoredOverlay.js, MultiColumnFilteringSelect.js, SingleTimeFieldTextBox.js, TimeField.js, CalendarWithTime.js, DatePicker.js, FormBuilder.js, `_BasePicker.js` (1822 lines), `_BaseSinglePicker.js`, `_BaseListPicker.js`, `_FormSectionField.js`, `_FormSectionLayout.js`, `_DateTextBox.js`, `_DateTimeTextBox.js`, `_DateTimeRange.js`, `_DateTimeRangeMixin.js`, `_RangeSliderMixin.js`, `_BaseIPInputWidget.js`, `_DependentDateTimePicker.js`, `_AnchoredOverlayMainContainer.js`, plus IP validation helpers (`IPv6Validation.js` 712 lines, `IPv6MaskValidation.js`, `_SingleTimeValidation.js`).
  - `xwt/widget/table/` — Cisco's custom table/grid framework. See §5.
  - `xwt/widget/treegrid/` — TreeGrid.js (1464 lines), TreeGridStore.js, GlobalToolbar.js, ContextualToolbar.js, ContextualButtonGroup.js, Ribbon.js, QuickFilter.js, FilterUtil.js, RowEdit.js, PopoverIntegration.js, QuickViewIntegration.js, `_DetailWidgetMixin.js`, `_ManageFilterDialog.js`, `_SaveFilterDialog.js`, `_MoveToRowDropdown.js`, `_Filter.js`, `_IndirectSelectColumn.js`, `_Dod.js`, `_DeleteConfirm.js`, plus `templates/ContextualToolbar.html`, `GlobalToolbar.html`, `MoveTo.html`.
  - `xwt/widget/tree/` — Tree.js, TreeNode.js, TreePanel.js, `_Tree.js`, `_TreeNode.js`, ForestStoreModel.js, BidirectionalForestStoreModel.js, dndAvatar.js, dndSource.js, Avatar.js; plus `templates/TreeNode.html`, `TreePanel.html`.
  - `xwt/widget/layout/` — XwtContentPane.js, XwtTabContainer.js, XwtScrollingTabController.js, BorderContainer mirror, SplitContainer.js, AccordionContainer.js, AccordionPane.js, TitlePane.js, Popover.js (3334 lines), BaseOverlay.js, ContextualOverlay.js, Dialog.js, Container360.js, View360.js, PageHeader.js, PagenotFound.js, Dashlet.js, DashletDialogSettings.js, DashletSettings.js, DashboardPanel.js, DesignLaunchPad.js, Carousel.js, MetricPanel.js, ProgressBall.js, Breadcrumb.js, ListScroller.js, AbridgedShell.js, OverlayObserverFactory.js, TabContentPane.js, `_360Container.js`, `_BasePanel.js`, `_CarouselItem.js`, `_PopoverButton.js`, `_Scroller.js`, `_TabToolbarButton.js`, `_popoverPlace.js`, plus `layout/quickview/` (ActionPanel.js, Panel.js, PropertiesPanel.js). `layout/templates/` holds the full HTML shell templates.
  - `xwt/widget/navigation/` — SlideMenu.js (2394 lines), Toolbar.js, ToolbarButton.js, Breadcrumb.js, AlertBar.js, AlarmsFormatter.js, Formatter.js, Gadget.js, GadgetItem.js, UIshell.js, `_ToolbarContainer.js`, plus `_slidemenu/` (Panel.js, MenuItem.js, IndexContainer.js, FavoritesContainer.js, ControlsPanel.js, SearchField.js, Ribbon.js) and `_breadcrumb/` (Folder.js, Item.js).
  - `xwt/widget/uishell/` — Header.js (524 lines), DropContainer.js, GlobalBreadcrumb.js, Notification.js, Search.js, SearchDropDown.js, SearchDropDownItem.js, SearchOptions.js, SearchResults.js. This is the chrome — header, search, notifications, breadcrumb.
  - `xwt/widget/notification/` — Alert.js, ErrorMessage.js, Form.js, ProgressBar.js, Toaster.js, ValidationTextBox.js.
  - `xwt/widget/datagrid/` — wraps dojox grid (see §5).
  - `xwt/widget/charting/` — large custom charting: action2d/, axis2d/, dashlet2d/, gridChart/, metricChart/, plot2d/, scaler/, themes/, widget/; headline files include `gridChart/Grid.js` (584 lines), `gridChart/Panel.js` (2645 lines), `gridChart/GenericChart.js`, `gridChart/ExportPlugin.js` (1168 lines), MetricChart.js (932 lines), plus themes Prime.js, PrimePattern.js, PrimeStatus.js, PrimeStatusPattern.js, PrimeStatusTranslucent.js, PrimeTranslucent.js, Reboot.js, RebootPattern.js, etc.
  - `xwt/widget/tasknavigator/` — Task.js, TaskArrow.js, TaskNavigator.js (1312 lines), TaskNavigatorVertical.js. This is the wizard/stepper primitive — critical for Inventory device-add.
  - `xwt/widget/dashboard/` — Dashboard.js, DashboardConfig.js, SimpleAccordion.js, `_ActionItem.js`, `_ConfigActionGroup.js`.
  - `xwt/widget/filtertoolbar/` — FilterToolbar.js (861 lines).
  - `xwt/widget/keywordtokenfield/` — KeywordTokenField.js, `_KeywordTokenField.js`.
  - `xwt/widget/menu/` — MenuItem.js, MenuItemLabel.js, PopupMenuItem.js.
  - `xwt/widget/objectselector/` — ObjectSelector.js (6929 lines) — the huge device/object picker used across EPNM — plus `_ObjectSelectorList.js` (2413 lines), `_ObjectSelectorTree.js` (2025 lines), `_ObjectSelectorStore.js` (1620 lines), `_ObjectSelectorListView.js` (1653 lines), `_ObjectSelectorListItem.js`, `_ObjectSelectorTreeNode.js` (1059 lines), `_ObjectSelectorToolbar.js`, `_ObjectSelectorDnDController.js`, `_CheckedCache.js`, `_ForestStoreModel.js` (791 lines), `_dndSelector.js`, `_dndSource.js`, `_StoreDataItem.js`, `_SelectionDisplayBar.js`, `_Standby.js`, `_Titlebar.js`, `DataFieldMap.js`, `_OSMenuItem.js`, `_utilMixin.js`.
  - `xwt/widget/quickview/` — QuickView.js (1995 lines), QuickViewActionItem.js.
  - `xwt/widget/repeater/` — DataRepeater.js (4415 lines), DataRepeaterPlus.js, Repeater.js, RepeaterItem.js, RepeaterItemPlus.js, RepeaterRowActionsControl.js, RepeaterRowEditControl.js, RepeaterRowSimpleActionsControl.js, RepeaterRowStateControl.js.
  - `xwt/widget/persistedstate/` — PersistedStateDataStore.js, DefaultPersistedStateDataStore.js, CookieBackedPersistedStateDataStore.js, `_PersistStateMixin.js`. User-preference persistence.
  - `xwt/widget/shared/` — filter/, help/, layout/, menu/ cross-cutting helpers. Filter subtree has AdvancedFilterPanel.js (667 lines), FilterPopover.js (532 lines), FilterWidget.js (310 lines), utils.js.
  - `xwt/widget/toolbar/` — LayoutToolbar.js, Toolbar.js.
  - `xwt/widget/visualize/` — cluster/Cluster.js (1090 lines), matrix/Matrix.js, parallelCoordinates/ParallelCoordinates.js, tree/Tree.js (2208 lines), tree/`_TreeDragDrop.js`, `_D3Base.js` (1490 lines), plus d3.js, backbone.js, underscore.js trampolines.
  - `xwt/widget/treemap/` — TreeMapPanel.js, Treemap.js.
  - `xwt/widget/gauges/` — Analog/Glossy/Reboot/Bar gauges (~25 files).
  - `xwt/widget/form/uploader/` — HTML5/IFrame upload plugins.
  - `xwt/widget/form/_picker/`, `xwt/widget/form/_anchoredoverlay/`, `xwt/widget/form/_listbox/` — shared picker internals (ObjectSelectorMultiPickerMixin.js, ObjectSelectorSinglePickerMixin.js, TableMultiPickerMixin.js, TableSinglePickerMixin.js, `_BaseList.js`, `_BasePickerPopover.js`).
  - Top-level rollup entry points: `xwt.js`, `xwt.profile.js` (502 lines), `xwt-core.js`, `xwt-common.js`, `xwt-form.js`, `xwt-layout.js`, `xwt-charts.js`, `xwt-table.js`, `xwt-treetable.js`, `xwt-tasknavigator.js`, `xwt-shell.js`, `xwt-visualization.js`, `xwt-objectselector.js`, `xwt-repeater.js`, `xwt-login.js`.
  - `xwt/themes/prime/` — CSS theme (see §3).
  - `xwt/nls/` — NLS (I18N) properties.

- `ui/core/ui_components/lib/xwtx/` — thin XWT extensions. WcsMenuTree.js, XwtGlobalUtility.js, XWTXProperties.js, captureUtil.js, xwtx.profile.js.

- `ui/core/ui_components/lib/prime/` — Cisco Prime designer/runtime widgets on top of XWT. Subtrees: `css/` (designer.css, prime.css, prime-XWT33x.css, icons.css, resourceManager.css, adjustStyleForStorm.css), `nls/` (ApplicationProperties.js, CEProvisioningProperties.js 3438 lines, ResourceManagerProperties.js, RulesManagerProperties.js — multi-locale), `widget/` (Designer.js 4504 lines, UiCommon.js 7646 lines, UiPropertyForms.js 880 lines, UiRuntimeBase.js 2109 lines, UiRuntimeOptical.js, UiRuntimeProfiles.js, `_ApplicationPropertiesMixin.js`, `_i18nPrimeMixin.js`; `widget/form/FormBuilder.js`, `HyperlinkTextBox.js`; `widget/notification/ProgressBar.js`, `_i18nAjaxMessageParserMixin.js`, `_i18nNotificationMixin.js`; `widget/resourceManager/` 18+ files including ResourcePropertyForm.js 967 lines, TableColumnSelector.js 971 lines, ResourceContainer.js 668 lines; `widget/rulesManager/RulesContainer.js`, `RulesPanel.js` 690 lines; `widget/table/ContextualButtonGroup.js`, `ContextualToolbar.js`, `EditableTable.js` 844 lines, `FormatterLib.js`; `widget/userpreference/ProvisioningUserPreference.js`; `widget/dojo/data/` (ItemFileWriteAndMoveStore.js, ItemFileWriteSaveToUrlStore.js, `_StoreMixin.js` 1214 lines); `widget/dojox/rpc/EasyPagingRest.js`, `DefaultHooks.js`), `utils/` (RestUtility.js, `_ObjectMixin.js`, `_StringMixin.js`), and top-level `UiUtils.js` (1494 lines).

- `ui/core/ui_components/lib/codemirror/` — CodeMirror editor (drools hint mode, SQL hint, etc.) — used in the rules editor, not in Inventory/Fault.

- `ui/core/ui_components/lib/gridx/` — gridx library (`Grid.js` 225 lines plus `GridCommon.js`, `allModules.js`, `gridx.profile.js`, and subtrees with pagination/filter templates `PaginationBar.html`, `QuickFilter.html`, `LinkPager.html`).

- `ui/core/ui_components/lib/html2canvas/` — html2canvas for chart export.

- `ui/core/ui_components/lib/util/` — Dojo build tools (buildscripts/, checkstyle/, docscripts/, doh/, jsdoc/, shrinksafe/).

- `ui/core/ui_components/build/` — `build.bat`, `build.sh`, `build.xml` (99 lines). See §9.

- `ui/core/ui_designer/` — the UI designer webapp. `java/src/com/cisco/prime/uidesign/Download.java`, `Upload.java`; `web/` subtree.

- `ui/core/ui_xde_client/` — the XDE client bridge to provisioning backend.

- `ui/apps/` — sample/embedded apps using the framework: `bulkPromote/`, `customermanager/`, `emsmanager/`, `forceDelete/`, `profilemanager/`, `resourcemanager/`, `servicemanager/`. Each app has `applications/<Name>/js/`, `css/`, `nls/`, `.jsp`. This shows the app-scaffolding pattern.

Representative directory paths (verbatim):
- `ui/core/ui_components/lib/dijit/form/`
- `ui/core/ui_components/lib/dijit/layout/`
- `ui/core/ui_components/lib/dojox/grid/`
- `ui/core/ui_components/lib/xwt/widget/table/`
- `ui/core/ui_components/lib/xwt/widget/treegrid/`
- `ui/core/ui_components/lib/xwt/widget/form/`
- `ui/core/ui_components/lib/xwt/widget/layout/`
- `ui/core/ui_components/lib/xwt/widget/uishell/`
- `ui/core/ui_components/lib/xwt/widget/navigation/`
- `ui/core/ui_components/lib/xwt/widget/objectselector/`
- `ui/core/ui_components/lib/xwt/widget/tasknavigator/`
- `ui/core/ui_components/lib/xwt/themes/prime/`
- `ui/core/ui_components/lib/prime/widget/`

## 3. Theme / Styling Foundations

The branded theme is `xwt/themes/prime/`. Complete CSS file organization:

- `ui/core/ui_components/lib/xwt/themes/prime/` rollup/import stylesheets:
  - `prime.css` (26 lines), `prime-xwt.css`, `prime-xwt-print.css`, `prime-base.css`, `prime-explorer.css`, `prime_rtl.css`
  - `importBase.css`, `importDojo.css`, `importExplorer.css`, `importXwt.css`, `importXwtForm.css`, `importXwtLayout.css`, `importXwtLogin.css`, `importXwtNotification.css`, `importXwtUishell.css`, `importXwtVisualization.css`
  - top-level component overrides: `Common.css` (210 lines), `Dialog.css` (342 lines), `Dialog_rtl.css`, `LoginLite.css`, `Menu.css`, `Menu_rtl.css`, `TitlePane.css`, `TitlePane_rtl.css`, `Toolbar.css`

- `ui/core/ui_components/lib/xwt/themes/prime/xwt/` component theme subtree:
  - `form/` — 35+ files: Button.css (369), Checkbox.css, CheckedMultiSelect.css, Common.css (361), MultipleFileUpload.css (771), Numberspinner.css, RadioButton.css, RangeSlider.css, Select.css, anchoredoverlay2.css (207), baselistpicker.css (205), basepicker.css (481), basesinglepicker.css (346), combobox.css (265), combobutton.css, datefield.css, datepicker.css (219), datetimerange.css, dropdown.css (281), formBuilder.css, groupbox.css, iconbutton.css, icondropdownbutton.css, ipv6.css, listbox.css, menubutton.css (186), quickviewhint.css, singletimefield.css, slider.css (712), starrating.css, textboxhint.css, textbutton.css (452), textbuttongroup.css, texticonbutton.css, timefield.css, unifiedIp.css.
  - `layout/` — BorderContainer.css (64), Container360.css (238), ContentPane.css, PageHeader.css (28), PagenotFound.css, TabContainer.css (223), TabContainer_rtl.css, accordion.css, accordioncontainer.css (281), breadcrumb.css, carousel.css (199), dashlet.css (264), designlaunchpad.css (201), layout.css, popover.css (436), progressball.css, quickview.css (235), splitcontainer.css, tabs.css (506), titlepane.css (246), view360.css (182), viewContainer360.css (210), xwtpanels.css.
  - `navigation/` — Breadcrumb.css (163), alertbar.css (126), menuitem.css (268), slidemenu.css (630), toolbar.css (236).
  - `uishell/` — Header.css (392), Search.css (278).
  - `table/` — **Table.css (1748 lines), Toolbar.css (1580 lines)**. These are the big ones for Inventory + Alarms table styling.
  - `treegrid/treeGrid.css` (877).
  - `treemap/treemap.css`, `tree/dnd.css`, `tree/treepanel.css` (650).
  - `grid/enhancedgrid.css` (764) — legacy dojox enhanced grid theme.
  - `chart/` — action.css, charts.css (690), gridChart.css (353).
  - `notification/` — alert.css (237), errorMessage.css, notification.css (282), progressBar.css, toaster.css.
  - `tasknavigator/Task.css` (374), `TaskNavigator.css` (287).
  - `objectselector/objectselector.css` (958), `objectselectortoolbar.css` (533).
  - `quickview/quickview.css` (520), `repeater/repeater.css` (488).
  - `filtertoolbar/filtertoolbar.css` (445), `keywordtokenfield/keywordtokenfield.css` (247).
  - `shared/filter/filterpopover.css`, `shared/filter/filterwidget.css`, `shared/menu/SlideMenuPopup.css`.
  - `toolbar/layouttoolbar.css`, `tasknavigator/`, `visualize/` per-visualization CSS.
  - `iconFonts/` — `fonts.css` (594), `loginFonts.css`, `fontAwesome/css/font-awesome.css` (1482).
  - Page-level CSS: `aboutpage.css` (305), `calendar.css` (444), `dashboardConfig.css` (469), `login.css` (330), `menu.css`, `navigation.css`, `refimpl.css` (542), `search.css`, `servertime.css`, `uishell.css`.

Files with names suggesting the blue-and-white EPNM theme (names are evidence only):
- No files named `blue.css` / `white.css` / `epnm-theme.css` at the prime-theme level. The Prime theme is organized **by component, not by color variant**. Color variables (e.g. blues) would be baked into each component CSS file and into the font/palette configuration. The legacy dojox charting themes do include `dojox/charting/themes/PlotKit/blue.js` (7 lines) and `BlueDusk.js` (13 lines) but those are chart palettes, not page chrome.
- The legacy claro/nihilo/soria/tundra Dijit theme directories exist (`ui/core/ui_components/lib/dijit/themes/claro/...`) — blue-ish — but they are **not** the Prime theme; they are stock Dojo baseline. Prime.css imports/overrides these.
- Blue iconography: `dojox/mobile/themes/.../DomButtonBlueBadge.css`, `DomButtonBlueBall.css`, `DomButtonBlueCircleArrow.css`, `DomButtonBlueCircleMinus.css`, `DomButtonBlueCirclePlus.css`, `DomButtonDarkBlueCheck.css`, `DomButtonDarkBlueCheck_rtl.css` — mobile-theme button icons, likely not loaded in the desktop EPNM chrome.

Typography / layout grids / component skins: the `prime/xwt/iconFonts/fonts.css` (594 lines) and `uishell/Header.css` (392 lines) are the typography + chrome entry points. `Common.css` (210 at theme root, 361 under form/) is the typography/base-reset layer. `refimpl.css` (542 lines) is likely the reference-implementation page layout sampler.

## 4. Layout Primitives

Shell pieces Inventory and Fault Management would sit inside:

- **Header** — `ui/core/ui_components/lib/xwt/widget/uishell/Header.js` (524 lines). Templates: `xwt/widget/templates/uishell/header.html` (28 lines), `categoryItem.html`, `globalBreadcrumb.html`, `notification.html`, `search.html`, `searchActionItem.html`, `searchOptions.html`, `searchResultItem.html`, `searchResults.html`. CSS: `xwt/themes/prime/xwt/uishell/Header.css` (392).
- **Left-nav / menu tree** — `xwt/widget/navigation/SlideMenu.js` (2394 lines) with `_slidemenu/` subtree (Panel.js 382, IndexContainer.js 456, MenuItem.js 798, FavoritesContainer.js, ControlsPanel.js, SearchField.js, Ribbon.js); `xwtx/widget/WcsMenuTree.js` appears to be a compatibility wrapper. CSS: `navigation/slidemenu.css` (630), `navigation/menuitem.css` (268), `shared/menu/SlideMenuPopup.css`.
- **Global breadcrumb** — `xwt/widget/uishell/GlobalBreadcrumb.js` (416); component `xwt/widget/navigation/Breadcrumb.js` (412) and `_breadcrumb/Item.js`, `Folder.js`.
- **Toolbar** — `xwt/widget/navigation/Toolbar.js` (686), `ToolbarButton.js`, `_ToolbarContainer.js` (335); `xwt/widget/toolbar/LayoutToolbar.js` (416), `Toolbar.js` (173). Plus the big table-specific toolbars (see §5). CSS: `navigation/toolbar.css` (236), `toolbar/layouttoolbar.css`.
- **Page frame** — `xwt/widget/layout/PageHeader.js` (142, `PageHeader.html`, `PageHeader.css` 28), `XwtContentPane.js` (177), `XwtTabContainer.js` (341), `XwtScrollingTabController.js` (810), `AbridgedShell.js` (56, `AbridgedShell.html`), `Container360.js` (420, `Container360.html` 38, `Container360.css` 238), `View360.js` (285, `view360.css` 182), `PagenotFound.js`. `xwt/widget/templates/layout/` has AccordionContainer.html, AccordionPane.html, Breadcrumb.html, Carousel.html, ContextualOverlay.html, Dashlet.html, Dashlet2x2.html, DesignLaunchPad.html, MetricPanelCarousel.html, PageHeader.html, PagenotFound.html, Popover.html, TitlePane.html, XwtContentPane.html, XwtScrollingTabController.html, `_360Container.html`, `_ScrollingTabToolbarButton.html`, `_TabButton.html`.
- **Dialog** — `xwt/widget/layout/Dialog.js` (715, `templates/layout/Dialog.html` 19, `Dialog.css` 342, `Dialog_rtl.css`). Overlay stack: `BaseOverlay.js` (882), `ContextualOverlay.js`, `OverlayObserverFactory.js` (115), `Popover.js` (3334, `Popover.html` 38, `popover.css` 436), `_popoverPlace.js` (503), `_PopoverButton.js`.
- **Tabs / Stack / Accordion / Split** — `AccordionContainer.js` (356), `AccordionPane.js` (559, `AccordionPane.html` 28, `accordioncontainer.css` 281), `SplitContainer.js` (521, `splitcontainer.css`), `TitlePane.js` (708, `TitlePane.html` 16, `titlepane.css` 246).
- **Alert bar, Notification, Toaster** — `xwt/widget/navigation/AlertBar.js` (312, `alertbar.css` 126); `xwt/widget/notification/Toaster.js` (294, `toaster.css` 182), `Alert.js` (609, `alert.css` 237), `ErrorMessage.js`, `ProgressBar.js`, `Form.js`, `ValidationTextBox.js`.
- **Task Navigator (wizard)** — `xwt/widget/tasknavigator/TaskNavigator.js` (1312), `Task.js` (660), `TaskArrow.js`, `TaskNavigatorVertical.js` (329). Templates `Task.html` (38), `TaskArrow.html`, `TaskNavigator.html` (17). CSS `tasknavigator/Task.css` (374), `TaskNavigator.css` (287). Required for Inventory device-add wizard.
- **Dashlet / Dashboard** — `xwt/widget/layout/Dashlet.js` (944), `DashletDialogSettings.js`, `DashletSettings.js`, `DashboardPanel.js`, `MetricPanel.js` (658, `MetricPanelCarousel.html`); `xwt/widget/dashboard/Dashboard.js` (211), `DashboardConfig.js` (622), `SimpleAccordion.js`. CSS `layout/dashlet.css` (264), `dashboardConfig.css` (469).

## 5. Table / Grid Primitives

EPNM runs three generations of table widgets side-by-side. The POC Alarms table and Network-Devices table almost certainly sit on the XWT Table (the most recent generation).

**Generation 1 — Stock dojox.grid DataGrid** (`ui/core/ui_components/lib/dojox/grid/`):
- `DataGrid.js` (663), `EnhancedGrid.js` (264), `TreeGrid.js` (972), `LazyTreeGrid.js` (844), `LazyTreeGridStoreModel.js`, `_Grid.js` (1396), `_View.js` (858), `_ViewManager.js` (309), `_Scroller.js` (505), `_Builder.js` (762), `_Layout.js` (275), `_Events.js` (508), `_FocusManager.js` (641), `_EditManager.js`, `_RowManager.js`, `_RowSelector.js`, `_Selector.js`, `_CheckBoxSelector.js`, `_RadioSelector.js`, `_SelectionPreserver.js`, `_TreeView.js` (464), `Selection.js`, `TreeSelection.js`, `DataSelection.js`, `cells.js`, `util.js`, `BidiSupport.js`. Plugins under `dojox/grid/enhanced/` — per-locale NLS (EnhancedGrid.js 13-line stubs across 20+ locale dirs), templates (ClearFilterConfirmPane.html, CriteriaBox.html, FilterBar.html, FilterBoolValueBox.html, FilterDefPane.html, FilterStatusPane.html, Pagination.html), `_Events.js`, `_FocusManager.js` (787), `_Plugin.js`, `_PluginManager.js` (275). Theme CSS `dojox/grid/resources/Grid.css` (428), `claroGrid.css` (323), `nihiloGrid.css`, `soriaGrid.css`, `tundraGrid.css`.

**Generation 2 — Prime EnhancedGridWrapper** (`ui/core/ui_components/lib/xwt/widget/datagrid/`):
- `EnhancedGrid.js` (595), `EnhancedGridWrapper.js` (610), `PopoverIntegration.js` (1214), `QuickViewIntegration.js` (751), `LoadingIndicator.js` (130), `cells.js`, `patches.js`. Templates `enhancedGridWrapper.html`, `LoadingIndicator.html`. Prime theme CSS `xwt/themes/prime/xwt/grid/enhancedgrid.css` (764).

**Generation 3 — XWT Table (the current EPNM table)** (`ui/core/ui_components/lib/xwt/widget/table/`):
- Core: `Table.js` (5146 lines) — the main table widget, `TableWrapper.js` (388), `PageTable.js` (653).
- Columns: `Column.js` (705), `Columns.js` (657), `ColumnTypes.js`, `ColumnFormatters.js`, `ExpanderColumn.js` (496), `IndexColumn.js`, `SelectorColumn.js`, `_ColumnAvatar.js`, `_ColumnMover.js` (296), `_ColumnResizer.js`.
- Editing: `Edit.js` (1577), `EditorMixin.js`, `_DeleteConfirm.js`, `_MoveToRowDropdown.js`.
- Filtering/sorting: `Filter.js` (254), `Filters.js` (635), `FilterByExample.js` (529), `FilterEngine.js` (322), `FilteringToolbar.js`, `FilteringWrapperStore.js` (213), `Sort.js` (216), `_FilterButton.js`, `_FilterMap.js`, `_FilterWidget.js` (268), `_ByExampleWidget.js` (402), `_ByExampleWidgetPicker.js`, `_ByExampleDateTimeRangePicker.js`, `_ByExampleOSWidgetPicker.js`, `_ByExampleTableWidgetPicker.js`, `_ManageFilterDialog.js` (232), `_SaveFilterDialog.js` (183).
- Toolbars / integrations: `GlobalToolbar.js` (914), `ContextualToolbar.js` (1515), `ContextualButtonGroup.js` (1147), `Ribbon.js` (411), `PopoverIntegration.js` (1121), `QuickViewIntegration.js` (711), `Select.js` (1213), `DetailMixin.js`, `Meta.js`, `LoadingIndicator.js` (154), `util.js`, `Toolbar.js` (13 — shim).
- Templates: `xwt/widget/table/templates/ContextualToolbar.html` (37), `FilterByExample.html`, `FilteringToolbar.html` (25), `GlobalToolbar.html` (30), `LoadingIndicator.html`, `MoveTo.html`, `PageTable.html` (18), `Table.html` (33), `_ByExampleWidget.html`, `_FilterWidget.html` (24), `tableWrapper.html`.
- Theme CSS: `xwt/themes/prime/xwt/table/Table.css` (1748), `Toolbar.css` (1580). These two files are the master style for every Inventory/Alarms table in EPNM.

**TreeGrid equivalent** (`xwt/widget/treegrid/`) — same pattern, rides on top of Table.js. Used for hierarchical inventory views.

**gridx** (`ui/core/ui_components/lib/gridx/` — `Grid.js` 225) is present but appears to be an alternative stack used rarely; the main table is XWT Table.js.

Both **alarms tables and network-devices tables** in classic Inventory/Fault would almost certainly be instances of `xwt/widget/table/Table.js` with custom column configs, a FilteringToolbar or FilterByExample pane, a GlobalToolbar/ContextualToolbar button set, and PopoverIntegration for row details.

## 6. Form Widgets

The device-add wizard (Inventory create-device form) would compose these XWT form widgets (see §2 for full list; highlights here):

- Text input: `xwt/widget/form/TextBoxHint.js` (594) for the standard textbox with placeholder/hint; Dijit `ValidationTextBox.js` (331) as the fallback; Prime-specific `xwt/widget/notification/ValidationTextBox.js` (464) for validation-with-toast.
- IP + MAC: `IPAddress.js` (299), `IPv4TextBox.js` (284), `IPv6TextBox.js`, `IPv6Address.js`, `IPv6AddressWithMask.js` (351), `IPv6Validation.js` (712), `IPv6MaskValidation.js` (76), `UnifiedIPAddress.js` (1246), `MacTextBox.js` (326), `_BaseIPInputWidget.js` (188). Dedicated templates `xwt/widget/templates/form/IPv6AddressWithMask.html`, `UnifiedIPAddress.html`.
- Select / picker: `ComboBox.js` (584), `FilteringSelect.js` (619), `DropDown.js` (394), `MultiColumnFilteringSelect.js` (452), `CheckedMultiSelect.js` (596), `CheckBoxGroup.js` (434), `RadioButtonGroup.js` (410), `ListBox.js` (220), pickers `TableSinglePicker.js`, `TableMultiPicker.js`, `TableMultiPickerList.js`, `ObjectSelectorSinglePicker.js`, `ObjectSelectorMultiPicker.js`, `ObjectSelectorMultiPickerList.js`, plus underlying `_BasePicker.js` (1822), `_BaseSinglePicker.js` (584), `_BaseListPicker.js` (328), `_BaseList.js` (684), `_BasePickerPopover.js` (141), mixins `ObjectSelectorSinglePickerMixin.js` (392), `ObjectSelectorMultiPickerMixin.js` (699), `TableSinglePickerMixin.js` (214), `TableMultiPickerMixin.js` (696).
- Date/time: `DateTextBox.js` (415), `DateField.js` (932), `DatePicker.js` (903), `DateTimePicker.js` (951), `DateTimeRangePicker.js`, `CalendarWithTime.js` (613), `TimeField.js` (1016), `SingleTimeFieldTextBox.js` (821), `_DateTextBox.js`, `_DateTimeTextBox.js`, `_DateTimeRange.js` (303), `_DateTimeRangeMixin.js` (445), `_DependentDateTimePicker.js`, `_SingleTimeValidation.js` (692).
- Numeric: `NumberTextBox.js` (70), `NumberSpinner.js` (74).
- Password: `PasswordTextBox.js` (214).
- Buttons: `TextButton.js`, `IconButton.js`, `IconDropDownButton.js`, `MenuButton.js`, `TextIconButton.js` (258), `TextButtonGroup.js`, `ToggleButtonGroup.js` (208), `ToggleLink.js` (348).
- Slider / range: `HorizontalSlider.js`, `VerticalSlider.js`, `HorizontalRangeSlider.js` (283), `VerticalRangeSlider.js` (290), `_RangeSliderMixin.js` (408), `_SliderBarMover.js`, `_SliderMoverMax.js`, `HorizontalRuleLabels.js`, `VerticalRuleLabels.js`.
- Form structure: `FormBuilder.js` (460), `GroupBox.js` (134), `Label.js`, `_FormSectionField.js` (772), `_FormSectionLayout.js` (328), `QuickViewHint.js` (279).
- Upload: `MultipleFileUpload.js` (1006), `MultiUploaderBase.js`, `MultiUploaderFileList.js` (1142), `_MultipleFileUploadPluginManager.js`, `uploader/plugins/HTML5.js`, `IFrame.js`.
- Misc: `Rating.js` (184), `AnchoredOverlay.js` (1595).

All are templated widgets; HTML in `xwt/widget/templates/form/`. CSS per-widget in `xwt/themes/prime/xwt/form/`.

## 7. Pub/Sub and Event-Bus Framework

Direct matches:

- `ui/core/ui_components/lib/dojo/topic.js` (38 lines). Stock Dojo topic API — `topic.publish()` / `topic.subscribe()`.
- `ui/core/ui_components/lib/dojo/lang/async/topic.js` (41 lines). Async wrapper around topic.
- `ui/core/ui_components/lib/dojo/_base/connect.js` (374 lines). Legacy `dojo.connect` / `dojo.publish` bridge.
- `ui/core/ui_components/lib/dojo/router.js` (28 lines). Framework routing — maps URL hashes to app views; relevant for deep-linking from Inventory to Fault.
- `ui/core/ui_components/lib/dojo/Evented.js` and `dojo/on.js` (per the tree report's dojo structure, implied by `_WidgetBase.js`'s event patterns) are the emit/on infrastructure used throughout XWT widgets.

No custom Cisco-namespace pub/sub wrapper visible as a dedicated directory. The event-bus coupling between Inventory and Fault panes (e.g. "device selected here → alarms pane refreshes there") is almost certainly implemented via **`dojo/topic` topic strings** inside individual XWT widgets plus `_WidgetBase.emit()` events. Candidate integration points: `xwt/widget/objectselector/_ObjectSelectorStore.js` (1620) likely publishes selection topics; `xwt/widget/table/Table.js` (5146) and `xwt/widget/navigation/AlarmsFormatter.js` (103) mention Alarms in the tree — that file may subscribe to alarm-count topics for the header badge.

Invisible-coupling risk for the execution session: the execution session must grep the real source (not just this tree) for `topic.publish(`, `topic.subscribe(`, `dojo/topic`, and `emit(` calls to map the event surface. Names in the tree show the plumbing exists but not the topic names.

## 8. Client-Side Utilities

- I18N / NLS: 
  - Stock CLDR: `ui/core/ui_components/lib/dojo/cldr/nls/` with per-locale buddhist/chinese/coptic/currency/ethiopic/generic/gregorian/hebrew/indian/islamic/japanese/number/persian/roc files (~25 locales).
  - Dijit NLS: `ui/core/ui_components/lib/dijit/nls/common.js` (44), `loading.js` (42), plus `dijit/form/nls/` per-locale ComboBox.js, Textarea.js, validate.js; `dijit/_editor/nls/` for editor commands.
  - XWT NLS: `ui/core/ui_components/lib/xwt/nls/XWTProperties.js` (647) and per-locale variants (da/de/es-es/fr/it/nl/pt-br/sv-se/zh/zh-tw), `XWTDateTimePatterns.js`, `XWTDateTime.js`; `xwt/nls/XWTProperties.js` is the master key table.
  - xwtx NLS: `ui/core/ui_components/lib/xwtx/nls/XWTXProperties.js`.
  - Prime NLS: `ui/core/ui_components/lib/prime/nls/ApplicationProperties.js` (116), `CEProvisioningProperties.js` (3438), `ResourceManagerProperties.js` (193), `RulesManagerProperties.js` (454), per-locale en/en-gb/en-us/ja/ko.
  - Application-specific NLS: `ui/apps/<app>/applications/<App>/nls/<App>Properties.js` per locale (en, en-gb, en-us, ja, ko).
  - I18N mixins: `xwt/widget/_i18nMixin.js`, `i18nMixin.js`, `prime/widget/_i18nPrimeMixin.js`, `prime/widget/notification/_i18nAjaxMessageParserMixin.js`, `_i18nNotificationMixin.js`.

- Formatting: `xwt/widget/table/ColumnFormatters.js` (114), `prime/widget/table/FormatterLib.js` (125), `xwt/widget/navigation/Formatter.js` (27), `xwt/widget/navigation/AlarmsFormatter.js` (103). Also `dojox/html/format.js`, `dojo/date.js`, `dojo/number.js`, `dojo/currency.js` (stock).

- Validation: `xwt/widget/form/IPv6Validation.js` (712), `_SingleTimeValidation.js` (692), `IPv6MaskValidation.js`, plus `dijit/form/nls/*/validate.js` locale-specific messages. Dijit `_FormMixin.js` (454) + `ValidationTextBox.js` (331) = core form-level validation.

- Utilities:
  - `xwt/widget/CommonUtilities.js` (825), `xwt/widget/util.js` (232), `xwt/captureUtil.js` (97), `xwt/debugSwitcher.js`, `xwtx/captureUtil.js`, `xwtx/widget/XwtGlobalUtility.js`.
  - `xwt/widget/_ZIndexMixin.js`, `_ZIndexMixinHelper.js`, `_ConfigureTheme.js`, `_SmallWindow.js`, `TooltipDialog.js`, `DijitPatches.js`, `_PasswordResetDialog.js`.
  - `prime/widget/utils/RestUtility.js`, `_ObjectMixin.js`, `_StringMixin.js`; `prime/UiUtils.js` (1494).
  - Persistence: `xwt/widget/persistedstate/` (`PersistedStateDataStore.js`, `DefaultPersistedStateDataStore.js`, `CookieBackedPersistedStateDataStore.js`, `_PersistStateMixin.js`) for user-preference persistence.
  - REST/store: `prime/widget/dojox/rpc/EasyPagingRest.js` (428), `DefaultHooks.js`; `prime/widget/dojo/data/ItemFileWriteAndMoveStore.js` (310), `ItemFileWriteSaveToUrlStore.js` (301), `_StoreMixin.js` (1214).

## 9. Build System

- **Maven** is the top-level orchestrator. Every module has `pom.xml`: root `pom.xml` (46), `build/` parent `pom.xml`, `ui/pom.xml` (31), `ui/apps/pom.xml` (35), `ui/core/ui_components/` child poms including `pom-standalone.xml` (47), `pom-standalone-xwt.xml` (156), `pom-DEPRECATED.xml`, `pom-origin-changed to-storm.xml`, `pom.xml` (47). Build props in `build/build.properties` (49), `mvn-settings.xml` (57), `ivysettings.xml` (17).
- **Dojo builder** under `ui/core/ui_components/lib/util/`. `build.js` (372), `build.sh` (6), `build.bat` (3), `build_release.sh` (140), `cdnBuild.sh`, `jslib/buildUtil.js` (2022), `buildUtilXd.js`, `i18nUtil.js` (334), `fileUtil.js`. Dojo profile files: `ui/core/ui_components/build/globals.properties` (5), `options.properties` (8); profile manifests `xwt.profile.js` (502), `xwtx.profile.js` (38), `dijit.profile.js` (35), and per-layer `xwt-core.js`, `xwt-common.js`, `xwt-form.js`, etc. as profile layers.
- **Ant** (legacy) — `build/build-ui.xml` (58), `build/build-macros.xml` (106), `ui/core/ui_components/build/build.xml` (99), `ui/core/ui_designer/build/build.xml` (90), `lib/build/`. Used to wrap the Dojo build step into the Maven lifecycle.
- **Ivy** (legacy) — `build/ivysettings.xml` (17); individual modules include `ivy.xml` (e.g. `ui/core/ProvisioningUIController/ivy.xml`).
- **Shell scripts** — `build/block_root_user.sh` (67), various `build.sh`/`build.bat` per subtree.
- **Assembly descriptors** — `assembly.xml`, `assembly-standalone.xml`, `assembly-standalone-xwt.xml`, `assembly-storm.xml` per app/module. These drive the packaging output.
- **CheckStyle + SonarQube** — `ui/core/ui_components/lib/util/checkstyle/` (`checkstyleUtil.js` 764, `runCheckstyle.js`, `checkstyleReport.html`), `xmp-pp-helper/.settings/org.sonar.ide.eclipse.core.prefs`, `xmp-pp-helper/.checkstyle`.
- **Eclipse project metadata** everywhere: `.project`, `.classpath`, `.settings/org.eclipse.*` — the repo assumes Eclipse IDE as the primary dev environment.

## 10. What to Read First

For the execution session to understand EPNM's visual identity before theming the Angular classic view, open these five in order:

1. **`ui/core/ui_components/lib/xwt/themes/prime/xwt/table/Table.css`** (1748 lines) — The single biggest theme file in the repo. Every Inventory and Alarms table gets its colors, spacing, border, hover, selection, striping, header/cell chrome from here. This file *is* the Prime visual identity for data tables. Pair with `xwt/themes/prime/xwt/table/Toolbar.css` (1580 lines).

2. **`ui/core/ui_components/lib/xwt/themes/prime/prime.css`** + **`importXwt.css`** + **`Common.css`** — the entry-point rollups. Read these to see how Prime composes the theme (imports stock Dojo Common, overrides with Prime Common, loads per-component overrides). Typography, base color vars, resets live here.

3. **`ui/core/ui_components/lib/xwt/widget/table/Table.js`** (5146 lines) and its template `xwt/widget/table/templates/Table.html` (33 lines). The DOM structure Prime Tables generate — what classes exist, what's a `thead`/`tbody` vs. a div-grid, what selectors the Angular rebuild must emit to reuse the CSS if that path is taken.

4. **`ui/core/ui_components/lib/xwt/widget/uishell/Header.js`** (524) + its template `xwt/widget/templates/uishell/header.html` (28) + `xwt/themes/prime/xwt/uishell/Header.css` (392). The branded top chrome — logo placement, search bar, notifications, user menu. Critical for the classic shell look.

5. **`ui/core/ui_components/lib/xwt/widget/navigation/SlideMenu.js`** (2394) + `xwt/widget/navigation/_slidemenu/Panel.js` (382), `IndexContainer.js` (456), `MenuItem.js` (798) + CSS `xwt/themes/prime/xwt/navigation/slidemenu.css` (630). The left-nav that sits around Inventory and Fault screens.

Honorable mentions (consult after these five): `xwt/widget/tasknavigator/TaskNavigator.js` (wizard style for Inventory device-add), `xwt/widget/objectselector/ObjectSelector.js` (6929 — the giant device picker), `xwt/widget/layout/Popover.js` (3334 — row-detail popovers in tables), `xwt/widget/form/_BasePicker.js` (1822 — all pickers derive from this), and `dojo/topic.js` + a grep of the real codebase for `topic.publish(` to reveal the event-bus topic names.

## Issues / Caveats

- The report's header path is a macOS path (`/Users/cmoore/Documents/...`), confirming this is a local mirror snapshot; line counts and file names are verbatim.
- Names are evidence, not proof. `xwt/widget/navigation/AlarmsFormatter.js` (103 lines) is the only named "Alarms" file I found in the framework layer — the rest of the Fault Management table is almost certainly a generic `xwt/widget/table/Table.js` instance configured by a Fault-module app (not in this repo). The Inventory network-devices table is likely the same. This repo is the **framework + sample apps**, not the Inventory or Fault feature modules themselves.
- The tree report says `pf-framework` but the majority of the tree (demo/, driver/, discovery/, multivendorsupport/, lib/) is the **provisioning engine**, not UI framework. Only `ui/` is UI. This may indicate the transcripts' "PI framework" concept covers more than just UI, or that Colin's team conflated the combined provisioning-plus-UI repo with just the UI layer. Worth confirming.
- No top-level file named anything like `epnm-theme.css` or `blue-white.css`. The EPNM "blue-and-white" identity is distributed across the Prime theme — color values are embedded in individual component CSS files and the `iconFonts/fonts.css` (594) typography file. Extracting a palette will require reading the actual CSS, not inferring from filenames.
- Three grid generations coexist (dojox DataGrid, EnhancedGridWrapper, XWT Table). Feature modules may use any of them. Execution session should confirm which generation the Inventory Network Devices table and the Fault Alarms table actually use.
- No dedicated `prime/blue.css` or EPNM-theme variable file surfaced. The `variables.less` (378 lines) at `dijit/themes/claro/variables.less` is Dojo's claro variables, not Prime.
- `visualize/` subtree pulls d3/backbone/underscore trampolines — legacy topology visualizations. Not needed for tabular Inventory/Fault rebuild.
