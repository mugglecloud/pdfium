// Copyright 2016 PDFium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Original code copyright 2014 Foxit Software Inc. http://www.foxitsoftware.com

#include "xfa/fxfa/parser/cxfa_captiondata.h"

#include "xfa/fxfa/parser/cxfa_font.h"
#include "xfa/fxfa/parser/cxfa_margin.h"
#include "xfa/fxfa/parser/cxfa_measurement.h"
#include "xfa/fxfa/parser/cxfa_node.h"
#include "xfa/fxfa/parser/cxfa_value.h"

CXFA_CaptionData::CXFA_CaptionData(CXFA_Node* pNode) : CXFA_DataData(pNode) {}

bool CXFA_CaptionData::IsVisible() const {
  return m_pNode->JSObject()
             ->TryEnum(XFA_Attribute::Presence, true)
             .value_or(XFA_AttributeEnum::Visible) ==
         XFA_AttributeEnum::Visible;
}

bool CXFA_CaptionData::IsHidden() const {
  return m_pNode->JSObject()
             ->TryEnum(XFA_Attribute::Presence, true)
             .value_or(XFA_AttributeEnum::Visible) == XFA_AttributeEnum::Hidden;
}

XFA_AttributeEnum CXFA_CaptionData::GetPlacementType() const {
  return m_pNode->JSObject()
      ->TryEnum(XFA_Attribute::Placement, true)
      .value_or(XFA_AttributeEnum::Left);
}

float CXFA_CaptionData::GetReserve() const {
  return m_pNode->JSObject()
      ->GetMeasure(XFA_Attribute::Reserve)
      .ToUnit(XFA_Unit::Pt);
}

CXFA_Margin* CXFA_CaptionData::GetMargin() const {
  return m_pNode ? m_pNode->GetChild<CXFA_Margin>(0, XFA_Element::Margin, false)
                 : nullptr;
}

CXFA_FontData CXFA_CaptionData::GetFontData() const {
  return CXFA_FontData(
      m_pNode ? m_pNode->GetChild<CXFA_Font>(0, XFA_Element::Font, false)
              : nullptr);
}

CXFA_Value* CXFA_CaptionData::GetValue() const {
  return m_pNode ? m_pNode->GetChild<CXFA_Value>(0, XFA_Element::Value, false)
                 : nullptr;
}
