from collections import OrderedDict

grammar = OrderedDict(
    {
        "Telheader_Quelle": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "Telheader_Ziel": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_destination",
        },
        "Telheader_TelSeq": {
            "type": "int",
            "length": 6,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_sequence_number",
        },
        "Telheader_AnlZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_current_datetime",
        },
        "Satzart": {
            "type": "str",
            "length": 9,
            "dp": False,
            "ubl_path": False,
            "df_val": "AUSK00056",
            "df_func": False,
        },
        "RxAusk_AusId_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "ubl_path": False,
            "df_val": "000",
            "df_func": False,
        },
        "RxAusk_AusId_AusNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "ubl_path": "DespatchAdvice.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_AusId_HostAusKz": {
            "type": "str",
            "length": 5,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "RxAusk_ExtRef": {
            "type": "str",
            "length": 20,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:OrderReference.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_AUTYP_Typ": {
            "type": "str",
            "length": 6,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cac:ShipmentStage."
            "cbc:TransportMeansTypeCode",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_KST_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "ubl_path": False,
            "df_val": "000",
            "df_func": False,
        },
        "RxAusk_KST_KuNr": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty."
            "cbc:CustomerAssignedAccountID",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Name": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name",
        },
        "RxAusk_Adrs_Name2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name2",
        },
        "RxAusk_Adrs_Name3": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name3",
        },
        "RxAusk_Adrs_Name4": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name4",
        },
        "RxAusk_Adrs_Anrede": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PartyName.cbc:Title",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Adr": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Adr",
        },
        "RxAusk_Adrs_Adr2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_PLZ": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cbc:PostalZone",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Ort": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cbc:CityName",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_OrtTeil": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Land": {
            "type": "str",
            "length": 4,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Tel": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:Contact.cbc:Telephone",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Email": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:DeliveryContact."
            "cbc:ElectronicMail",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_Fax": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_WWW": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Adrs_ILN": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Name": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PartyName.cbc:Name",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Name2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name2",
        },
        "RxAusk_LiefAdrs_Name3": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name3",
        },
        "RxAusk_LiefAdrs_Name4": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Name4",
        },
        "RxAusk_LiefAdrs_Anrede": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PartyName.cbc:Title",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Adr": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_Adrs_Adr",
        },
        "RxAusk_LiefAdrs_Adr2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_PLZ": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cbc:PostalZone",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Ort": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cbc:CityName",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_OrtTeil": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cbc:CountrySubentity",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Land": {
            "type": "str",
            "length": 4,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:PostalAddress.cac:Country.cbc:IdentificationCode",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Tel": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:Contact.cbc:Telephone",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Email": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:Contact.cbc:ElectronicMail",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_Fax": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DeliveryCustomerParty.cac:Party."
            "cac:Contact.cbc:Telefax",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_WWW": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefAdrs_ILN": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Name": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Name2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Name3": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Name4": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Anrede": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Adr": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Adr2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_PLZ": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Ort": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_OrtTeil": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Land": {
            "type": "str",
            "length": 4,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Tel": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Email": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_Fax": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_WWW": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_EndEmpfAdrs_ILN": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_GeplBereitTerm": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": [
                "DespatchAdvice.cac:Shipment.cac:Delivery."
                "cac:EstimatedDeliveryPeriod.cbc:EndDate",
                "DespatchAdvice.cac:Shipment.cac:Delivery."
                "cac:EstimatedDeliveryPeriod.cbc:EndTime",
            ],
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_GeplEinStrat_LagRf": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cac:Delivery.cac:Despatch."
            "cac:DespatchLocation.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_Info2Wamas": {
            "type": "str",
            "length": 77,
            "dp": False,
            "ubl_path": "DespatchAdvice.cbc:Note",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_AbladeStelle": {
            "type": "str",
            "length": 30,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_LiefTerm": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:DeliveryInstructions",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_BestZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:OrderReference.cbc:IssueDate",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_ZustellTermin": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:DeliveryInstructions",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_ZustellZeitpunkt": {
            "type": "str",
            "length": 5,
            "dp": False,
            "ubl_path": False,
            "df_val": "FRUEH",
            "df_func": False,
        },
        "RxAusk_BereitstellTermin": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:DeliveryInstructions",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_BereitstellZeitpunkt": {
            "type": "str",
            "length": 5,
            "dp": False,
            "ubl_path": False,
            "df_val": "FRUEH",
            "df_func": False,
        },
        "RxAusk_RahmenTourId_TourNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourId_HostTourKz": {
            "type": "str",
            "length": 5,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "RxAusk_RahmenTour_WA_Tor": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourMaxGew": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:GrossWeightMeasure",
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourMaxStdLE": {
            "type": "float",
            "length": 7,
            "dp": 3,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourStdLEVol": {
            "type": "float",
            "length": 7,
            "dp": 3,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourFzId1": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourFzId2": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTour_LKWT_LkwTyp": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourLkwFahrer": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTourLkwBeifahrer": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_RahmenTour_S_SchichtId": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_VerlRfNr": {
            "type": "int",
            "length": 3,
            "dp": False,
            "ubl_path": False,
            "df_val": 1,
            "df_func": False,
        },
        "RxAusk_Prio": {
            "type": "str",
            "length": 1,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:Shipment.cbc:ShippingPriorityLevelCode",
            "df_val": False,
            "df_func": False,
        },
        "RxAuskI_Text": {
            "type": "str",
            "length": 70,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_MergeId": {
            "type": "str",
            "length": 30,
            "dp": False,
            "ubl_path": {
                "DespatchAdvice.cac:Shipment.cbc:HandlingInstructions": [
                    "DespatchAdvice.cac:Shipment.cbc:ID",
                    False,
                ]
            },
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_VAST_Versandart": {
            "type": "str",
            "length": 2,
            "dp": False,
            "ubl_path": False,
            "df_val": "ST",
            "df_func": False,
        },
        "RxAusk_Gepl2Step_LagRf": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxAusk_VplStrat": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": False,
            "df_val": "Def_Strat",
            "df_func": False,
        },
    }
)
