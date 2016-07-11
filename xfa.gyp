{
  "variables": {
    "chromium_code": 1,
    "pdf_enable_v8%": 1,
     "variables": {
      'clang_use_chrome_plugins': 1,
    },
  },
  "target_defaults": {
    "defines": [
      "PDF_ENABLE_XFA",
    ],
    'msvs_disabled_warnings': [
      4267,
    ],
  },
  "targets":[
    {
      "target_name":"xfa",
      "type":"static_library",
      'include_dirs': [
        # This is implicit in GN.
        '<(DEPTH)',
        '.',
        'third_party/freetype/include',
        'third_party/freetype/include/freetype',
        '<(DEPTH)/v8',
        '<(DEPTH)/v8/include',
      ],
      'defines' : [
        'FT2_BUILD_LIBRARY',
      ],
      'dependencies': [
        '<(DEPTH)/v8/src/v8.gyp:v8',
      ],
      'export_dependent_settings': [
        '<(DEPTH)/v8/src/v8.gyp:v8',
      ],
      "sources":[
        "fxjse/class.cpp",
        "fxjse/context.cpp",
        "fxjse/context.h",
        "fxjse/dynprop.cpp",
        "fxjse/include/cfxjse_arguments.h",
        "fxjse/include/cfxjse_class.h",
        "fxjse/include/cfxjse_value.h",
        "fxjse/include/fxjse.h",
        "fxjse/runtime.cpp",
        "fxjse/runtime.h",
        "fxjse/scope_inline.h",
        "fxjse/value.cpp",
        "xfa/fde/cfde_path.cpp",
        "xfa/fde/cfde_path.h",
        "xfa/fde/cfde_txtedtbuf.cpp",
        "xfa/fde/cfde_txtedtbuf.h",
        "xfa/fde/cfde_txtedtbufiter.cpp",
        "xfa/fde/cfde_txtedtbufiter.h",
        "xfa/fde/cfde_txtedtdorecord_deleterange.cpp",
        "xfa/fde/cfde_txtedtdorecord_deleterange.h",
        "xfa/fde/cfde_txtedtdorecord_insert.cpp",
        "xfa/fde/cfde_txtedtdorecord_insert.h",
        "xfa/fde/cfde_txtedtengine.cpp",
        "xfa/fde/cfde_txtedtengine.h",
        "xfa/fde/cfde_txtedtpage.cpp",
        "xfa/fde/cfde_txtedtpage.h",
        "xfa/fde/cfde_txtedtparag.cpp",
        "xfa/fde/cfde_txtedtparag.h",
        "xfa/fde/cfde_txtedttextset.cpp",
        "xfa/fde/cfde_txtedttextset.h",
        "xfa/fde/cfx_chariter.cpp",
        "xfa/fde/cfx_chariter.h",
        "xfa/fde/cfx_wordbreak.cpp",
        "xfa/fde/cfx_wordbreak.h",
        "xfa/fde/css/fde_css.cpp",
        "xfa/fde/css/fde_css.h",
        "xfa/fde/css/fde_csscache.cpp",
        "xfa/fde/css/fde_csscache.h",
        "xfa/fde/css/fde_cssdatatable.cpp",
        "xfa/fde/css/fde_cssdatatable.h",
        "xfa/fde/css/fde_cssdeclaration.cpp",
        "xfa/fde/css/fde_cssdeclaration.h",
        "xfa/fde/css/fde_cssstyleselector.cpp",
        "xfa/fde/css/fde_cssstyleselector.h",
        "xfa/fde/css/fde_cssstylesheet.cpp",
        "xfa/fde/css/fde_cssstylesheet.h",
        "xfa/fde/css/fde_csssyntax.cpp",
        "xfa/fde/css/fde_csssyntax.h",
        "xfa/fde/fde_gedevice.cpp",
        "xfa/fde/fde_gedevice.h",
        "xfa/fde/fde_iterator.cpp",
        "xfa/fde/fde_iterator.h",
        "xfa/fde/fde_object.h",
        "xfa/fde/fde_render.cpp",
        "xfa/fde/fde_render.h",
        "xfa/fde/ifde_txtedtdorecord.h",
        "xfa/fde/ifde_txtedtengine.h",
        "xfa/fde/ifde_txtedtpage.h",
        "xfa/fde/ifx_chariter.h",
        "xfa/fde/tto/fde_textout.cpp",
        "xfa/fde/tto/fde_textout.h",
        "xfa/fde/xml/cfx_saxreader.cpp",
        "xfa/fde/xml/cfx_saxreader.h",
        "xfa/fde/xml/fde_xml.h",
        "xfa/fde/xml/fde_xml_imp.cpp",
        "xfa/fde/xml/fde_xml_imp.h",
        "xfa/fgas/crt/fgas_codepage.cpp",
        "xfa/fgas/crt/fgas_codepage.h",
        "xfa/fgas/crt/fgas_language.h",
        "xfa/fgas/crt/fgas_memory.cpp",
        "xfa/fgas/crt/fgas_memory.h",
        "xfa/fgas/crt/fgas_stream.cpp",
        "xfa/fgas/crt/fgas_stream.h",
        "xfa/fgas/crt/fgas_system.cpp",
        "xfa/fgas/crt/fgas_system.h",
        "xfa/fgas/crt/fgas_utils.cpp",
        "xfa/fgas/crt/fgas_utils.h",
        "xfa/fgas/font/fgas_font.h",
        "xfa/fgas/font/fgas_fontutils.cpp",
        "xfa/fgas/font/fgas_fontutils.h",
        "xfa/fgas/font/fgas_gefont.cpp",
        "xfa/fgas/font/fgas_gefont.h",
        "xfa/fgas/font/fgas_stdfontmgr.cpp",
        "xfa/fgas/font/fgas_stdfontmgr.h",
        "xfa/fgas/layout/fgas_linebreak.cpp",
        "xfa/fgas/layout/fgas_linebreak.h",
        "xfa/fgas/layout/fgas_rtfbreak.cpp",
        "xfa/fgas/layout/fgas_rtfbreak.h",
        "xfa/fgas/layout/fgas_textbreak.cpp",
        "xfa/fgas/layout/fgas_textbreak.h",
        "xfa/fgas/layout/fgas_unicode.cpp",
        "xfa/fgas/layout/fgas_unicode.h",
        "xfa/fgas/localization/fgas_datetime.cpp",
        "xfa/fgas/localization/fgas_datetime.h",
        "xfa/fgas/localization/fgas_locale.cpp",
        "xfa/fgas/localization/fgas_locale.h",
        "xfa/fgas/localization/fgas_localeimp.h",
        "xfa/fwl/basewidget/cfx_barcode.cpp",
        "xfa/fwl/basewidget/cfx_barcode.h",
        "xfa/fwl/basewidget/fwl_barcodeimp.cpp",
        "xfa/fwl/basewidget/fwl_barcodeimp.h",
        "xfa/fwl/basewidget/fwl_caretimp.cpp",
        "xfa/fwl/basewidget/fwl_caretimp.h",
        "xfa/fwl/basewidget/fwl_checkboximp.cpp",
        "xfa/fwl/basewidget/fwl_checkboximp.h",
        "xfa/fwl/basewidget/fwl_comboboximp.cpp",
        "xfa/fwl/basewidget/fwl_comboboximp.h",
        "xfa/fwl/basewidget/fwl_datetimepickerimp.cpp",
        "xfa/fwl/basewidget/fwl_datetimepickerimp.h",
        "xfa/fwl/basewidget/fwl_editimp.cpp",
        "xfa/fwl/basewidget/fwl_editimp.h",
        "xfa/fwl/basewidget/fwl_formproxyimp.cpp",
        "xfa/fwl/basewidget/fwl_formproxyimp.h",
        "xfa/fwl/basewidget/fwl_listboximp.cpp",
        "xfa/fwl/basewidget/fwl_listboximp.h",
        "xfa/fwl/basewidget/fwl_monthcalendarimp.cpp",
        "xfa/fwl/basewidget/fwl_monthcalendarimp.h",
        "xfa/fwl/basewidget/fwl_pictureboximp.cpp",
        "xfa/fwl/basewidget/fwl_pictureboximp.h",
        "xfa/fwl/basewidget/fwl_pushbuttonimp.cpp",
        "xfa/fwl/basewidget/fwl_pushbuttonimp.h",
        "xfa/fwl/basewidget/fwl_scrollbarimp.cpp",
        "xfa/fwl/basewidget/fwl_scrollbarimp.h",
        "xfa/fwl/basewidget/fwl_spinbuttonimp.cpp",
        "xfa/fwl/basewidget/fwl_spinbuttonimp.h",
        "xfa/fwl/basewidget/fwl_tooltipctrlimp.cpp",
        "xfa/fwl/basewidget/fwl_tooltipctrlimp.h",
        "xfa/fwl/basewidget/ifwl_barcode.h",
        "xfa/fwl/basewidget/ifwl_caret.h",
        "xfa/fwl/basewidget/ifwl_checkbox.h",
        "xfa/fwl/basewidget/ifwl_combobox.h",
        "xfa/fwl/basewidget/ifwl_datetimepicker.h",
        "xfa/fwl/basewidget/ifwl_edit.h",
        "xfa/fwl/basewidget/ifwl_listbox.h",
        "xfa/fwl/basewidget/ifwl_monthcalendar.h",
        "xfa/fwl/basewidget/ifwl_picturebox.h",
        "xfa/fwl/basewidget/ifwl_pushbutton.h",
        "xfa/fwl/basewidget/ifwl_scrollbar.h",
        "xfa/fwl/basewidget/ifwl_spinbutton.h",
        "xfa/fwl/basewidget/ifwl_tooltip.h",
        "xfa/fwl/core/cfwl_event.h",
        "xfa/fwl/core/cfwl_message.h",
        "xfa/fwl/core/cfwl_themebackground.h",
        "xfa/fwl/core/cfwl_themepart.h",
        "xfa/fwl/core/cfwl_themetext.h",
        "xfa/fwl/core/cfwl_widgetimpproperties.h",
        "xfa/fwl/core/cfwl_widgetmgr.cpp",
        "xfa/fwl/core/cfwl_widgetmgr.h",
        "xfa/fwl/core/fwl_appimp.cpp",
        "xfa/fwl/core/fwl_appimp.h",
        "xfa/fwl/core/fwl_error.h",
        "xfa/fwl/core/fwl_formimp.cpp",
        "xfa/fwl/core/fwl_formimp.h",
        "xfa/fwl/core/fwl_noteimp.cpp",
        "xfa/fwl/core/fwl_noteimp.h",
        "xfa/fwl/core/fwl_timerimp.cpp",
        "xfa/fwl/core/fwl_widgetdef.h",
        "xfa/fwl/core/fwl_widgetimp.cpp",
        "xfa/fwl/core/fwl_widgetimp.h",
        "xfa/fwl/core/ifwl_app.h",
        "xfa/fwl/core/ifwl_dataprovider.h",
        "xfa/fwl/core/ifwl_form.h",
        "xfa/fwl/core/ifwl_themeprovider.h",
        "xfa/fwl/core/ifwl_timer.h",
        "xfa/fwl/core/ifwl_widget.h",
        "xfa/fwl/core/ifwl_widgetdelegate.h",
        "xfa/fwl/core/include/fwl_widgethit.h",
        "xfa/fwl/core/include/ifwl_adaptertimermgr.h",
        "xfa/fwl/lightwidget/cfwl_barcode.cpp",
        "xfa/fwl/lightwidget/cfwl_barcode.h",
        "xfa/fwl/lightwidget/cfwl_checkbox.cpp",
        "xfa/fwl/lightwidget/cfwl_checkbox.h",
        "xfa/fwl/lightwidget/cfwl_combobox.cpp",
        "xfa/fwl/lightwidget/cfwl_combobox.h",
        "xfa/fwl/lightwidget/cfwl_datetimepicker.cpp",
        "xfa/fwl/lightwidget/cfwl_datetimepicker.h",
        "xfa/fwl/lightwidget/cfwl_edit.cpp",
        "xfa/fwl/lightwidget/cfwl_edit.h",
        "xfa/fwl/lightwidget/cfwl_listbox.cpp",
        "xfa/fwl/lightwidget/cfwl_listbox.h",
        "xfa/fwl/lightwidget/cfwl_picturebox.cpp",
        "xfa/fwl/lightwidget/cfwl_picturebox.h",
        "xfa/fwl/lightwidget/cfwl_pushbutton.cpp",
        "xfa/fwl/lightwidget/cfwl_pushbutton.h",
        "xfa/fwl/lightwidget/cfwl_widget.cpp",
        "xfa/fwl/lightwidget/cfwl_widget.h",
        "xfa/fwl/lightwidget/cfwl_widgetproperties.cpp",
        "xfa/fwl/lightwidget/cfwl_widgetproperties.h",
        "xfa/fwl/theme/cfwl_barcodetp.cpp",
        "xfa/fwl/theme/cfwl_barcodetp.h",
        "xfa/fwl/theme/cfwl_carettp.cpp",
        "xfa/fwl/theme/cfwl_carettp.h",
        "xfa/fwl/theme/cfwl_checkboxtp.cpp",
        "xfa/fwl/theme/cfwl_checkboxtp.h",
        "xfa/fwl/theme/cfwl_comboboxtp.cpp",
        "xfa/fwl/theme/cfwl_comboboxtp.h",
        "xfa/fwl/theme/cfwl_datetimepickedtp.cpp",
        "xfa/fwl/theme/cfwl_datetimepickertp.h",
        "xfa/fwl/theme/cfwl_edittp.cpp",
        "xfa/fwl/theme/cfwl_edittp.h",
        "xfa/fwl/theme/cfwl_listboxtp.cpp",
        "xfa/fwl/theme/cfwl_listboxtp.h",
        "xfa/fwl/theme/cfwl_monthcalendartp.cpp",
        "xfa/fwl/theme/cfwl_monthcalendartp.h",
        "xfa/fwl/theme/cfwl_pictureboxtp.cpp",
        "xfa/fwl/theme/cfwl_pictureboxtp.h",
        "xfa/fwl/theme/cfwl_pushbuttontp.cpp",
        "xfa/fwl/theme/cfwl_pushbuttontp.h",
        "xfa/fwl/theme/cfwl_scrollbartp.cpp",
        "xfa/fwl/theme/cfwl_scrollbartp.h",
        "xfa/fwl/theme/cfwl_utils.h",
        "xfa/fwl/theme/cfwl_widgettp.cpp",
        "xfa/fwl/theme/cfwl_widgettp.h",
        "xfa/fxbarcode/BC_Dimension.cpp",
        "xfa/fxbarcode/BC_Dimension.h",
        "xfa/fxbarcode/BC_Library.cpp",
        "xfa/fxbarcode/BC_TwoDimWriter.cpp",
        "xfa/fxbarcode/BC_TwoDimWriter.h",
        "xfa/fxbarcode/BC_UtilCodingConvert.cpp",
        "xfa/fxbarcode/BC_UtilCodingConvert.h",
        "xfa/fxbarcode/BC_Utils.cpp",
        "xfa/fxbarcode/BC_Writer.cpp",
        "xfa/fxbarcode/BC_Writer.h",
        "xfa/fxbarcode/cbc_codabar.cpp",
        "xfa/fxbarcode/cbc_codabar.h",
        "xfa/fxbarcode/cbc_code128.cpp",
        "xfa/fxbarcode/cbc_code128.h",
        "xfa/fxbarcode/cbc_code39.cpp",
        "xfa/fxbarcode/cbc_code39.h",
        "xfa/fxbarcode/cbc_codebase.cpp",
        "xfa/fxbarcode/cbc_codebase.h",
        "xfa/fxbarcode/cbc_datamatrix.cpp",
        "xfa/fxbarcode/cbc_datamatrix.h",
        "xfa/fxbarcode/cbc_ean13.cpp",
        "xfa/fxbarcode/cbc_ean13.h",
        "xfa/fxbarcode/cbc_ean8.cpp",
        "xfa/fxbarcode/cbc_ean8.h",
        "xfa/fxbarcode/cbc_onecode.cpp",
        "xfa/fxbarcode/cbc_onecode.h",
        "xfa/fxbarcode/cbc_pdf417i.cpp",
        "xfa/fxbarcode/cbc_pdf417i.h",
        "xfa/fxbarcode/cbc_qrcode.cpp",
        "xfa/fxbarcode/cbc_qrcode.h",
        "xfa/fxbarcode/cbc_upca.cpp",
        "xfa/fxbarcode/cbc_upca.h",
        "xfa/fxbarcode/common/BC_CommonBitArray.cpp",
        "xfa/fxbarcode/common/BC_CommonBitArray.h",
        "xfa/fxbarcode/common/BC_CommonBitMatrix.cpp",
        "xfa/fxbarcode/common/BC_CommonBitMatrix.h",
        "xfa/fxbarcode/common/BC_CommonByteArray.cpp",
        "xfa/fxbarcode/common/BC_CommonByteArray.h",
        "xfa/fxbarcode/common/BC_CommonByteMatrix.cpp",
        "xfa/fxbarcode/common/BC_CommonByteMatrix.h",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomon.cpp",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomon.h",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256.cpp",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256.h",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256Poly.cpp",
        "xfa/fxbarcode/common/reedsolomon/BC_ReedSolomonGF256Poly.h",
        "xfa/fxbarcode/datamatrix/BC_ASCIIEncoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_ASCIIEncoder.h",
        "xfa/fxbarcode/datamatrix/BC_Base256Encoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_Base256Encoder.h",
        "xfa/fxbarcode/datamatrix/BC_C40Encoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_C40Encoder.h",
        "xfa/fxbarcode/datamatrix/BC_DataMatrixSymbolInfo144.cpp",
        "xfa/fxbarcode/datamatrix/BC_DataMatrixSymbolInfo144.h",
        "xfa/fxbarcode/datamatrix/BC_DataMatrixWriter.cpp",
        "xfa/fxbarcode/datamatrix/BC_DataMatrixWriter.h",
        "xfa/fxbarcode/datamatrix/BC_DefaultPlacement.cpp",
        "xfa/fxbarcode/datamatrix/BC_DefaultPlacement.h",
        "xfa/fxbarcode/datamatrix/BC_EdifactEncoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_EdifactEncoder.h",
        "xfa/fxbarcode/datamatrix/BC_Encoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_Encoder.h",
        "xfa/fxbarcode/datamatrix/BC_EncoderContext.cpp",
        "xfa/fxbarcode/datamatrix/BC_EncoderContext.h",
        "xfa/fxbarcode/datamatrix/BC_ErrorCorrection.cpp",
        "xfa/fxbarcode/datamatrix/BC_ErrorCorrection.h",
        "xfa/fxbarcode/datamatrix/BC_HighLevelEncoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_HighLevelEncoder.h",
        "xfa/fxbarcode/datamatrix/BC_SymbolInfo.cpp",
        "xfa/fxbarcode/datamatrix/BC_SymbolInfo.h",
        "xfa/fxbarcode/datamatrix/BC_SymbolShapeHint.cpp",
        "xfa/fxbarcode/datamatrix/BC_SymbolShapeHint.h",
        "xfa/fxbarcode/datamatrix/BC_TextEncoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_TextEncoder.h",
        "xfa/fxbarcode/datamatrix/BC_X12Encoder.cpp",
        "xfa/fxbarcode/datamatrix/BC_X12Encoder.h",
        "xfa/fxbarcode/include/BC_Library.h",
        "xfa/fxbarcode/oned/BC_OneDimWriter.cpp",
        "xfa/fxbarcode/oned/BC_OneDimWriter.h",
        "xfa/fxbarcode/oned/BC_OnedCodaBarWriter.cpp",
        "xfa/fxbarcode/oned/BC_OnedCodaBarWriter.h",
        "xfa/fxbarcode/oned/BC_OnedCode128Writer.cpp",
        "xfa/fxbarcode/oned/BC_OnedCode128Writer.h",
        "xfa/fxbarcode/oned/BC_OnedCode39Writer.cpp",
        "xfa/fxbarcode/oned/BC_OnedCode39Writer.h",
        "xfa/fxbarcode/oned/BC_OnedEAN13Writer.cpp",
        "xfa/fxbarcode/oned/BC_OnedEAN13Writer.h",
        "xfa/fxbarcode/oned/BC_OnedEAN8Writer.cpp",
        "xfa/fxbarcode/oned/BC_OnedEAN8Writer.h",
        "xfa/fxbarcode/oned/BC_OnedUPCAWriter.cpp",
        "xfa/fxbarcode/oned/BC_OnedUPCAWriter.h",
        "xfa/fxbarcode/pdf417/BC_PDF417.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417.h",
        "xfa/fxbarcode/pdf417/BC_PDF417BarcodeMatrix.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417BarcodeMatrix.h",
        "xfa/fxbarcode/pdf417/BC_PDF417BarcodeRow.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417BarcodeRow.h",
        "xfa/fxbarcode/pdf417/BC_PDF417Compaction.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417Compaction.h",
        "xfa/fxbarcode/pdf417/BC_PDF417ErrorCorrection.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417ErrorCorrection.h",
        "xfa/fxbarcode/pdf417/BC_PDF417HighLevelEncoder.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417HighLevelEncoder.h",
        "xfa/fxbarcode/pdf417/BC_PDF417Writer.cpp",
        "xfa/fxbarcode/pdf417/BC_PDF417Writer.h",
        "xfa/fxbarcode/qrcode/BC_QRCodeWriter.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCodeWriter.h",
        "xfa/fxbarcode/qrcode/BC_QRCoder.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoder.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderBitVector.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderBitVector.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderBlockPair.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderBlockPair.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderECB.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderECB.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderECBlocks.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderECBlocks.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderEncoder.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderEncoder.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderErrorCorrectionLevel.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderErrorCorrectionLevel.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderMaskUtil.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderMaskUtil.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderMatrixUtil.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderMatrixUtil.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderMode.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderMode.h",
        "xfa/fxbarcode/qrcode/BC_QRCoderVersion.cpp",
        "xfa/fxbarcode/qrcode/BC_QRCoderVersion.h",
        "xfa/fxbarcode/utils.h",
        "xfa/fxfa/app/cxfa_eventparam.cpp",
        "xfa/fxfa/app/xfa_checksum.cpp",
        "xfa/fxfa/app/xfa_ffapp.cpp",
        "xfa/fxfa/app/xfa_ffbarcode.cpp",
        "xfa/fxfa/app/xfa_ffbarcode.h",
        "xfa/fxfa/app/xfa_ffcheckbutton.cpp",
        "xfa/fxfa/app/xfa_ffcheckbutton.h",
        "xfa/fxfa/app/xfa_ffchoicelist.cpp",
        "xfa/fxfa/app/xfa_ffchoicelist.h",
        "xfa/fxfa/app/xfa_ffdoc.cpp",
        "xfa/fxfa/app/xfa_ffdochandler.cpp",
        "xfa/fxfa/app/xfa_ffdocview.cpp",
        "xfa/fxfa/app/xfa_ffdraw.cpp",
        "xfa/fxfa/app/xfa_ffdraw.h",
        "xfa/fxfa/app/xfa_ffexclgroup.cpp",
        "xfa/fxfa/app/xfa_ffexclgroup.h",
        "xfa/fxfa/app/xfa_fffield.cpp",
        "xfa/fxfa/app/xfa_fffield.h",
        "xfa/fxfa/app/xfa_ffimage.cpp",
        "xfa/fxfa/app/xfa_ffimage.h",
        "xfa/fxfa/app/xfa_ffimageedit.cpp",
        "xfa/fxfa/app/xfa_ffimageedit.h",
        "xfa/fxfa/app/xfa_ffnotify.cpp",
        "xfa/fxfa/app/xfa_ffnotify.h",
        "xfa/fxfa/app/xfa_ffpageview.cpp",
        "xfa/fxfa/app/xfa_ffpath.cpp",
        "xfa/fxfa/app/xfa_ffpath.h",
        "xfa/fxfa/app/xfa_ffpushbutton.cpp",
        "xfa/fxfa/app/xfa_ffpushbutton.h",
        "xfa/fxfa/app/xfa_ffsignature.cpp",
        "xfa/fxfa/app/xfa_ffsignature.h",
        "xfa/fxfa/app/xfa_ffsubform.cpp",
        "xfa/fxfa/app/xfa_ffsubform.h",
        "xfa/fxfa/app/xfa_fftext.cpp",
        "xfa/fxfa/app/xfa_fftext.h",
        "xfa/fxfa/app/xfa_fftextedit.cpp",
        "xfa/fxfa/app/xfa_fftextedit.h",
        "xfa/fxfa/app/xfa_ffwidget.cpp",
        "xfa/fxfa/app/xfa_ffwidgetacc.cpp",
        "xfa/fxfa/app/xfa_ffwidgetacc.h",
        "xfa/fxfa/app/xfa_ffwidgethandler.cpp",
        "xfa/fxfa/app/xfa_fontmgr.cpp",
        "xfa/fxfa/app/xfa_fwladapter.cpp",
        "xfa/fxfa/app/xfa_fwladapter.h",
        "xfa/fxfa/app/xfa_fwltheme.cpp",
        "xfa/fxfa/app/xfa_fwltheme.h",
        "xfa/fxfa/app/xfa_rendercontext.cpp",
        "xfa/fxfa/app/xfa_textlayout.cpp",
        "xfa/fxfa/app/xfa_textlayout.h",
        "xfa/fxfa/fm2js/xfa_error.cpp",
        "xfa/fxfa/fm2js/xfa_error.h",
        "xfa/fxfa/fm2js/xfa_expression.cpp",
        "xfa/fxfa/fm2js/xfa_expression.h",
        "xfa/fxfa/fm2js/xfa_fm2jscontext.cpp",
        "xfa/fxfa/fm2js/xfa_fm2jscontext.h",
        "xfa/fxfa/fm2js/xfa_fmparse.cpp",
        "xfa/fxfa/fm2js/xfa_fmparse.h",
        "xfa/fxfa/fm2js/xfa_lexer.cpp",
        "xfa/fxfa/fm2js/xfa_lexer.h",
        "xfa/fxfa/fm2js/xfa_program.cpp",
        "xfa/fxfa/fm2js/xfa_program.h",
        "xfa/fxfa/fm2js/xfa_simpleexpression.cpp",
        "xfa/fxfa/fm2js/xfa_simpleexpression.h",
        "xfa/fxfa/include/cxfa_eventparam.h",
        "xfa/fxfa/include/fxfa.h",
        "xfa/fxfa/include/fxfa_basic.h",
        "xfa/fxfa/include/fxfa_widget.h",
        "xfa/fxfa/include/xfa_checksum.h",
        "xfa/fxfa/include/xfa_ffapp.h",
        "xfa/fxfa/include/xfa_ffdoc.h",
        "xfa/fxfa/include/xfa_ffdochandler.h",
        "xfa/fxfa/include/xfa_ffdocview.h",
        "xfa/fxfa/include/xfa_ffpageview.h",
        "xfa/fxfa/include/xfa_ffwidget.h",
        "xfa/fxfa/include/xfa_ffwidgethandler.h",
        "xfa/fxfa/include/xfa_fontmgr.h",
        "xfa/fxfa/include/xfa_rendercontext.h",
        "xfa/fxfa/parser/cxfa_arc.h",
        "xfa/fxfa/parser/cxfa_assist.cpp",
        "xfa/fxfa/parser/cxfa_assist.h",
        "xfa/fxfa/parser/cxfa_bind.cpp",
        "xfa/fxfa/parser/cxfa_bind.h",
        "xfa/fxfa/parser/cxfa_binditems.cpp",
        "xfa/fxfa/parser/cxfa_binditems.h",
        "xfa/fxfa/parser/cxfa_border.h",
        "xfa/fxfa/parser/cxfa_box.cpp",
        "xfa/fxfa/parser/cxfa_box.h",
        "xfa/fxfa/parser/cxfa_calculate.cpp",
        "xfa/fxfa/parser/cxfa_calculate.h",
        "xfa/fxfa/parser/cxfa_caption.cpp",
        "xfa/fxfa/parser/cxfa_caption.h",
        "xfa/fxfa/parser/cxfa_corner.h",
        "xfa/fxfa/parser/cxfa_data.cpp",
        "xfa/fxfa/parser/cxfa_data.h",
        "xfa/fxfa/parser/cxfa_edge.h",
        "xfa/fxfa/parser/cxfa_event.cpp",
        "xfa/fxfa/parser/cxfa_event.h",
        "xfa/fxfa/parser/cxfa_exdata.cpp",
        "xfa/fxfa/parser/cxfa_exdata.h",
        "xfa/fxfa/parser/cxfa_fill.cpp",
        "xfa/fxfa/parser/cxfa_fill.h",
        "xfa/fxfa/parser/cxfa_font.cpp",
        "xfa/fxfa/parser/cxfa_font.h",
        "xfa/fxfa/parser/cxfa_image.cpp",
        "xfa/fxfa/parser/cxfa_image.h",
        "xfa/fxfa/parser/cxfa_line.cpp",
        "xfa/fxfa/parser/cxfa_line.h",
        "xfa/fxfa/parser/cxfa_margin.cpp",
        "xfa/fxfa/parser/cxfa_margin.h",
        "xfa/fxfa/parser/cxfa_occur.cpp",
        "xfa/fxfa/parser/cxfa_occur.h",
        "xfa/fxfa/parser/cxfa_para.cpp",
        "xfa/fxfa/parser/cxfa_para.h",
        "xfa/fxfa/parser/cxfa_rectangle.h",
        "xfa/fxfa/parser/cxfa_script.cpp",
        "xfa/fxfa/parser/cxfa_script.h",
        "xfa/fxfa/parser/cxfa_stroke.cpp",
        "xfa/fxfa/parser/cxfa_stroke.h",
        "xfa/fxfa/parser/cxfa_submit.cpp",
        "xfa/fxfa/parser/cxfa_submit.h",
        "xfa/fxfa/parser/cxfa_text.cpp",
        "xfa/fxfa/parser/cxfa_text.h",
        "xfa/fxfa/parser/cxfa_tooltip.cpp",
        "xfa/fxfa/parser/cxfa_tooltip.h",
        "xfa/fxfa/parser/cxfa_validate.cpp",
        "xfa/fxfa/parser/cxfa_validate.h",
        "xfa/fxfa/parser/cxfa_value.cpp",
        "xfa/fxfa/parser/cxfa_value.h",
        "xfa/fxfa/parser/cxfa_valuearray.cpp",
        "xfa/fxfa/parser/cxfa_valuearray.h",
        "xfa/fxfa/parser/cxfa_widgetdata.cpp",
        "xfa/fxfa/parser/cxfa_widgetdata.h",
        "xfa/fxfa/parser/xfa_basic_data.cpp",
        "xfa/fxfa/parser/xfa_basic_data_attributes.cpp",
        "xfa/fxfa/parser/xfa_basic_data_element_attributes.cpp",
        "xfa/fxfa/parser/xfa_basic_data_element_properties.cpp",
        "xfa/fxfa/parser/xfa_basic_data_element_script.cpp",
        "xfa/fxfa/parser/xfa_basic_data_enum.cpp",
        "xfa/fxfa/parser/xfa_basic_data_packets.cpp",
        "xfa/fxfa/parser/xfa_basic_data.h",
        "xfa/fxfa/parser/xfa_basic_imp.cpp",
        "xfa/fxfa/parser/xfa_basic_imp.h",
        "xfa/fxfa/parser/xfa_doclayout.h",
        "xfa/fxfa/parser/xfa_document.h",
        "xfa/fxfa/parser/xfa_document_datamerger_imp.cpp",
        "xfa/fxfa/parser/xfa_document_datamerger_imp.h",
        "xfa/fxfa/parser/xfa_document_imp.cpp",
        "xfa/fxfa/parser/xfa_document_layout_imp.cpp",
        "xfa/fxfa/parser/xfa_document_layout_imp.h",
        "xfa/fxfa/parser/xfa_document_serialize.cpp",
        "xfa/fxfa/parser/xfa_document_serialize.h",
        "xfa/fxfa/parser/xfa_layout_appadapter.cpp",
        "xfa/fxfa/parser/xfa_layout_appadapter.h",
        "xfa/fxfa/parser/xfa_layout_itemlayout.cpp",
        "xfa/fxfa/parser/xfa_layout_itemlayout.h",
        "xfa/fxfa/parser/xfa_layout_pagemgr_new.cpp",
        "xfa/fxfa/parser/xfa_layout_pagemgr_new.h",
        "xfa/fxfa/parser/xfa_locale.cpp",
        "xfa/fxfa/parser/xfa_locale.h",
        "xfa/fxfa/parser/xfa_localemgr.cpp",
        "xfa/fxfa/parser/xfa_localemgr.h",
        "xfa/fxfa/parser/xfa_localevalue.cpp",
        "xfa/fxfa/parser/xfa_localevalue.h",
        "xfa/fxfa/parser/xfa_object.h",
        "xfa/fxfa/parser/xfa_object_imp.cpp",
        "xfa/fxfa/parser/xfa_parser_imp.cpp",
        "xfa/fxfa/parser/xfa_parser_imp.h",
        "xfa/fxfa/parser/xfa_script.h",
        "xfa/fxfa/parser/xfa_script_datawindow.cpp",
        "xfa/fxfa/parser/xfa_script_datawindow.h",
        "xfa/fxfa/parser/xfa_script_eventpseudomodel.cpp",
        "xfa/fxfa/parser/xfa_script_eventpseudomodel.h",
        "xfa/fxfa/parser/xfa_script_hostpseudomodel.cpp",
        "xfa/fxfa/parser/xfa_script_hostpseudomodel.h",
        "xfa/fxfa/parser/xfa_script_imp.cpp",
        "xfa/fxfa/parser/xfa_script_imp.h",
        "xfa/fxfa/parser/xfa_script_layoutpseudomodel.cpp",
        "xfa/fxfa/parser/xfa_script_layoutpseudomodel.h",
        "xfa/fxfa/parser/xfa_script_logpseudomodel.cpp",
        "xfa/fxfa/parser/xfa_script_logpseudomodel.h",
        "xfa/fxfa/parser/xfa_script_nodehelper.cpp",
        "xfa/fxfa/parser/xfa_script_nodehelper.h",
        "xfa/fxfa/parser/xfa_script_resolveprocessor.cpp",
        "xfa/fxfa/parser/xfa_script_resolveprocessor.h",
        "xfa/fxfa/parser/xfa_script_signaturepseudomodel.cpp",
        "xfa/fxfa/parser/xfa_script_signaturepseudomodel.h",
        "xfa/fxfa/parser/xfa_utils.h",
        "xfa/fxfa/parser/xfa_utils_imp.cpp",
        "xfa/fxgraphics/cagg_graphics.cpp",
        "xfa/fxgraphics/cagg_graphics.h",
        "xfa/fxgraphics/cfx_color.cpp",
        "xfa/fxgraphics/cfx_color.h",
        "xfa/fxgraphics/cfx_graphics.cpp",
        "xfa/fxgraphics/cfx_path.cpp",
        "xfa/fxgraphics/cfx_path.h",
        "xfa/fxgraphics/cfx_path_generator.cpp",
        "xfa/fxgraphics/cfx_path_generator.h",
        "xfa/fxgraphics/cfx_pattern.cpp",
        "xfa/fxgraphics/cfx_pattern.h",
        "xfa/fxgraphics/cfx_shading.cpp",
        "xfa/fxgraphics/cfx_shading.h",
        "xfa/fxgraphics/include/cfx_graphics.h",
      ],
      "conditions": [
        ["os_posix==1 and clang==0", { # When GCC
          'cflags': [ '-Wno-strict-overflow' ],
        }],
        ["OS == 'win'", {
          "configurations": {
            "Debug": {
              "msvs_configuration_attributes": {},
              "msvs_settings": {
                "VCCLCompilerTool": {},
                "VCLibrarianTool": {},
                "VCLinkerTool": {},
              }
            },
            "Release": {
              "msvs_configuration_attributes": {},
              "msvs_settings": {
                "VCCLCompilerTool": {},
                "VCLibrarianTool": {},
                "VCLinkerTool": {},
              }
            }
            },
          "sources": [],
        }],
        ["OS == 'mac'", {
          "configurations": {},
          "sources": [],
        }],
      ]
    }
  ]
}
