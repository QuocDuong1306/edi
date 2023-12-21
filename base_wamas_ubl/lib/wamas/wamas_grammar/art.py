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
            "df_val": False,
            "df_func": "get_sequence_number",
        },
        "Telheader_AnlZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "df_val": False,
            "df_func": "get_current_datetime",
        },
        "Satzart": {
            "type": "str",
            "length": 9,
            "dp": False,
            "df_val": "ART000061",
            "df_func": False,
        },
        "Art_AId_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": "000",
            "df_func": False,
        },
        "Art_AId_ArtNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AId_Var": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": "00000",
            "df_func": False,
        },
        "Art_ArtBez": {
            "type": "str",
            "length": 40,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ArtBez2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_IntArtBez": {
            "type": "str",
            "length": 40,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_Bestand_Einheit": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_Anzeige_Einheit": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_HOSTUNITS_HostEinh": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_HostGewKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_NettoGew": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AltAId_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AltAId_ArtNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AltAId_Var": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ArtTyp": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": "STD",
            "df_func": False,
        },
        "Art_SORT_Sortiment": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_BestErfArtWa": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": "STK",
            "df_func": False,
        },
        "Art_BestErfArtWe": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": "STK",
            "df_func": False,
        },
        "Art_BestKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AbcWert": {
            "type": "int",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": 999,
            "df_func": False,
        },
        "Art_AKS_ArtKlasse": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ArtGrp": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WAGRP_WaGrpId": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": "aSM",
            "df_func": False,
        },
        "Art_InvGrp": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": "-",
            "df_func": False,
        },
        "Art_AnbruchAnzErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ArtMischErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "J",
            "df_func": False,
        },
        "Art_AusPrMischErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "N",
            "df_func": False,
        },
        "Art_ChargeMischErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "J",
            "df_func": False,
        },
        "Art_ASCODE_ACode": {
            "type": "str",
            "length": 2,
            "dp": False,
            "dict_key": False,
            "df_val": "ANFRAGE",
            "df_func": False,
        },
        "Art_Aus_Schema": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": "ALL_WA",
            "df_func": False,
        },
        "Art_StdAus_LagRf": {
            "type": "str",
            "length": 15,
            "dp": False,
            "dict_key": False,
            "df_val": "sdDEF",
            "df_func": False,
        },
        "Art_TmpAus_LagRf": {
            "type": "str",
            "length": 15,
            "dp": False,
            "dict_key": False,
            "df_val": "sdDEF",
            "df_func": False,
        },
        "Art_AutoAbsKzWa": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ChangeAusPrErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ChargePflWa": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ChargePflWe": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_DisponentWe": {
            "type": "str",
            "length": 20,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_FifoFen": {
            "type": "int",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GanzTeMng": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GanzTeSplittKz1": {
            "type": "str",
            "length": 7,
            "dp": False,
            "dict_key": False,
            "df_val": "KANN",
            "df_func": False,
        },
        "Art_GanzTeSplittKz2": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": "ORIGTE",
            "df_func": False,
        },
        "Art_GewTolAbsWa": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 999999999,
            "df_func": False,
        },
        "Art_GewTolAbsWe": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 999999999,
            "df_func": False,
        },
        "Art_GewTolProzWa": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 50,
            "df_func": False,
        },
        "Art_GewTolProzWe": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 50,
            "df_func": False,
        },
        "Art_MaxDiffBasisAbsWa": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 999999999,
            "df_func": False,
        },
        "Art_MaxDiffBasisProzWa": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 999.9,
            "df_func": False,
        },
        "Art_MaxDiffGewAbsWa": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 999999999,
            "df_func": False,
        },
        "Art_MaxDiffGewProzWa": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 999.9,
            "df_func": False,
        },
        "Art_BestandTolAbsWe": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 999999999,
            "df_func": False,
        },
        "Art_BestandTolProzWe": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 999.9,
            "df_func": False,
        },
        "Art_Info": {
            "type": "str",
            "length": 77,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_LagWert": {
            "type": "float",
            "length": 14,
            "dp": 6,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_LBWE_LagIdWe": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": "eCAM",
            "df_func": False,
        },
        "Art_MhdMischErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "J",
            "df_func": False,
        },
        "Art_MHDPflWa": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "N",
            "df_func": False,
        },
        "Art_MHDPflWe": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_MinderCheckKzHost": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "N",
            "df_func": False,
        },
        "Art_MinderCheckKzLls": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "N",
            "df_func": False,
        },
        "Art_RefEinheit": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_RefMng": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_RestHaltProzWe": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": 100,
            "df_func": False,
        },
        "Art_RestHaltTaWa": {
            "type": "int",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_RestHaltTaWe": {
            "type": "int",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_SperrArtKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_SperrKzWa": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_StapelHoehe": {
            "type": "int",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_Stapelkzahl": {
            "type": "int",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": 100,
            "df_func": False,
        },
        "Art_SumGewErfWe": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ThmTauschErlWe": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_THM_ThmId": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_UeberLiefErlWe": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": "J",
            "df_func": False,
        },
        "Art_WartInt": {
            "type": "int",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WhrCode": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": "CHF",
            "df_func": False,
        },
        "Art_GefGutBuchs": {
            "type": "str",
            "length": 3,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutStoffBez": {
            "type": "str",
            "length": 70,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutStoffBez2": {
            "type": "str",
            "length": 70,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutStoffBez3": {
            "type": "str",
            "length": 70,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutChemBez": {
            "type": "str",
            "length": 70,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutEinh": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutKlassCode": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutKlasse": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutUnNr": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutVerpGrp": {
            "type": "str",
            "length": 10,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_GefGutZiffer": {
            "type": "str",
            "length": 9,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WaLvsSort_LvsSortiment": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": "-",
            "df_func": False,
        },
        "Art_SatzKz": {
            "type": "str",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_StapelGew": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": 99999,
            "df_func": False,
        },
        "Art_ARTSTAT_ArtStatGrp": {
            "type": "str",
            "length": 6,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_LgSchwelleProz": {
            "type": "float",
            "length": 4,
            "dp": 1,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_Batch": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_ArtKtoKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_MatqMischErl": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_AbschlStatus": {
            "type": "str",
            "length": 9,
            "dp": False,
            "dict_key": False,
            "df_val": "ANFRAGE",
            "df_func": False,
        },
        "Art_BestErfArtWh": {
            "type": "str",
            "length": 4,
            "dp": False,
            "dict_key": False,
            "df_val": "STK",
            "df_func": False,
        },
        "Art_ChargePflWh": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_MHDPflWh": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WhSerienNrKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WeSerienNrKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_WaSerienNrKz": {
            "type": "bool",
            "length": 1,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_PrueflosMngWe": {
            "type": "float",
            "length": 12,
            "dp": 3,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
        "Art_SNr_Einheit": {
            "type": "str",
            "length": 5,
            "dp": False,
            "dict_key": False,
            "df_val": False,
            "df_func": False,
        },
    }
)
