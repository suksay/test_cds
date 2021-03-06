#
# PySNMP MIB module LLDP-MIB-HUAWEI (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/LLDP-MIB-HUAWEI.mib
# Produced by pysmi-0.3.4 at Thu Jun 11 11:56:19 2020
# On host DESKTOP-LULODOL platform Linux version 4.19.84-microsoft-standard by user root
# Using Python version 3.7.3 (default, Dec 20 2019, 18:57:59) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
optixLogBoardId, optixLogSubCardId = mibBuilder.importSymbols("OPTIX-BOARD-MANAGE-MIB", "optixLogBoardId", "optixLogSubCardId")
optixProvisionPtn, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixProvisionPtn")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ObjectIdentity, Integer32, Unsigned32, Counter64, Bits, Gauge32, MibIdentifier, ModuleIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Integer32", "Unsigned32", "Counter64", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks")
TextualConvention, MacAddress, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "RowStatus")
optixPktLLDP = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27))
optixPktLLDP.setRevisions(('2012-04-20 00:00',))
if mibBuilder.loadTexts: optixPktLLDP.setLastUpdated('201204200000Z')
if mibBuilder.loadTexts: optixPktLLDP.setOrganization('Huawei Technologies co.,Ltd.')
optixPktLLDPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1))
optixLldpSendInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpSendInterval.setStatus('current')
optixLldpResetDelay = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpResetDelay.setStatus('current')
optixLldpTTLMilt = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpTTLMilt.setStatus('current')
optixLldpFastPduNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpFastPduNum.setStatus('current')
optixPKTLLDPTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5), )
if mibBuilder.loadTexts: optixPKTLLDPTable.setStatus('current')
optixPKTLLDPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1), ).setIndexNames((0, "LLDP-MIB-HUAWEI", "optixLldpBoardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpSubCardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpPortId"))
if mibBuilder.loadTexts: optixPKTLLDPEntry.setStatus('current')
optixLldpBoardId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixLldpBoardId.setStatus('current')
optixLldpSubCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 2), Unsigned32())
if mibBuilder.loadTexts: optixLldpSubCardId.setStatus('current')
optixLldpPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 3), Unsigned32())
if mibBuilder.loadTexts: optixLldpPortId.setStatus('current')
optixLldpWorkModle = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("tx", 1), ("rx", 2), ("txrx", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpWorkModle.setStatus('current')
optixLldpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpVlanId.setStatus('current')
optixLldpVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpVlanPri.setStatus('current')
optixLldpGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nb", 1), ("nntb", 2), ("ncb", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpGroupType.setStatus('current')
optixLldpPerReceiveMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpPerReceiveMsg.setStatus('current')
optixLldpSendMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpSendMsg.setStatus('current')
optixLldpLostMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpLostMsg.setStatus('current')
optixLldpErrMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpErrMsg.setStatus('current')
optixLldpAgeNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpAgeNeighbor.setStatus('current')
optixLldpLostTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpLostTlv.setStatus('current')
optixLldpUnknowTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixLldpUnknowTlv.setStatus('current')
optixLldpClrstatistic = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 5, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 255))).clone(namedValues=NamedValues(("clear", 1), ("invalid", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixLldpClrstatistic.setStatus('current')
optixPKTLldpNeigheorInfoEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 6))
optixPKTLldpNeigheorInfo = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 6, 1)).setObjects(("LLDP-MIB-HUAWEI", "optixLldpNeigheorInfoBoardId"), ("LLDP-MIB-HUAWEI", "optixLldpNeigheorInfoSubCardId"), ("LLDP-MIB-HUAWEI", "optixLldpNeigheorInfoPortId"), ("LLDP-MIB-HUAWEI", "optixLldpNeigheorInfoType"), ("LLDP-MIB-HUAWEI", "optixLldpNeigheorInfoNum"))
if mibBuilder.loadTexts: optixPKTLldpNeigheorInfo.setStatus('current')
optixPKTLldpNeigheorInfoTrapMember = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7))
optixLldpNeigheorInfoBoardId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: optixLldpNeigheorInfoBoardId.setStatus('current')
optixLldpNeigheorInfoSubCardId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: optixLldpNeigheorInfoSubCardId.setStatus('current')
optixLldpNeigheorInfoPortId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: optixLldpNeigheorInfoPortId.setStatus('current')
optixLldpNeigheorInfoType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("insert", 1), ("update", 2), ("delete", 3), ("drop", 4), ("ageout", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: optixLldpNeigheorInfoType.setStatus('current')
optixLldpNeigheorInfoNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 7, 5), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: optixLldpNeigheorInfoNum.setStatus('current')
optixPKTLLDPNeigheorInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8), )
if mibBuilder.loadTexts: optixPKTLLDPNeigheorInfoTable.setStatus('current')
optixPKTLLDPNeigheorInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1), ).setIndexNames((0, "LLDP-MIB-HUAWEI", "optixLldpBoardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpSubCardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpPortId"), (0, "LLDP-MIB-HUAWEI", "optixPKTLLDPNeigheorInfoIndex"))
if mibBuilder.loadTexts: optixPKTLLDPNeigheorInfoEntry.setStatus('current')
optixPKTLLDPNeigheorInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixPKTLLDPNeigheorInfoIndex.setStatus('current')
optixPKTLLDPLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPLastTime.setStatus('current')
optixPKTLLDPRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPRemainTime.setStatus('current')
optixPKTLLDPDestAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPDestAddrIndex.setStatus('current')
optixPKTLLDPChassisID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPChassisID.setStatus('current')
optixPKTLLDPPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPPortID.setStatus('current')
optixPKTLLDPPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPPortDescription.setStatus('current')
optixPKTLLDPSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPSystemName.setStatus('current')
optixPKTLLDPSystemDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPSystemDescription.setStatus('current')
optixPKTLLDPSystemCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPSystemCapabilities.setStatus('current')
optixPKTLLDPManagementAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPManagementAddress.setStatus('current')
optixPKTLLDPPortVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPPortVLANID.setStatus('current')
optixPKTLLDPPortAndProtocolVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPPortAndProtocolVLANID.setStatus('current')
optixPKTLLDPManagementVID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPManagementVID.setStatus('current')
optixPKTLLDPLinkAggregation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPLinkAggregation.setStatus('current')
optixPKTLLDPMACPHYConfigurationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPMACPHYConfigurationStatus.setStatus('current')
optixPKTLLDPMaximumFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 8, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPMaximumFrameSize.setStatus('current')
optixPKTLLDPBaseStationInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9), )
if mibBuilder.loadTexts: optixPKTLLDPBaseStationInfoTable.setStatus('current')
optixPKTLLDPBaseStationInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1), ).setIndexNames((0, "LLDP-MIB-HUAWEI", "optixLldpBoardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpSubCardId"), (0, "LLDP-MIB-HUAWEI", "optixLldpPortId"), (0, "LLDP-MIB-HUAWEI", "optixPKTLLDPOMIP"))
if mibBuilder.loadTexts: optixPKTLLDPBaseStationInfoEntry.setStatus('current')
optixPKTLLDPOMIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 1), IpAddress())
if mibBuilder.loadTexts: optixPKTLLDPOMIP.setStatus('current')
optixPKTLLDPSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPSysName.setStatus('current')
optixPKTLLDPOMMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPOMMAC.setStatus('current')
optixPKTLLDPMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPMTU.setStatus('current')
optixPKTLLDPOperMau = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPOperMau.setStatus('current')
optixPKTLLDPVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 1, 9, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPVlanID.setStatus('current')
optixPktLLDPNEGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 2))
optixPKTLLDPSysMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50, 27, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixPKTLLDPSysMacAddr.setStatus('current')
mibBuilder.exportSymbols("LLDP-MIB-HUAWEI", optixPKTLLDPBaseStationInfoTable=optixPKTLLDPBaseStationInfoTable, optixPKTLLDPDestAddrIndex=optixPKTLLDPDestAddrIndex, optixPKTLLDPSysName=optixPKTLLDPSysName, optixPKTLLDPSystemCapabilities=optixPKTLLDPSystemCapabilities, optixPKTLLDPLastTime=optixPKTLLDPLastTime, optixLldpErrMsg=optixLldpErrMsg, optixPKTLLDPMaximumFrameSize=optixPKTLLDPMaximumFrameSize, optixPKTLLDPLinkAggregation=optixPKTLLDPLinkAggregation, optixLldpFastPduNum=optixLldpFastPduNum, optixPKTLLDPRemainTime=optixPKTLLDPRemainTime, optixLldpSubCardId=optixLldpSubCardId, PYSNMP_MODULE_ID=optixPktLLDP, optixPKTLldpNeigheorInfoEvent=optixPKTLldpNeigheorInfoEvent, optixPKTLldpNeigheorInfoTrapMember=optixPKTLldpNeigheorInfoTrapMember, optixPKTLLDPChassisID=optixPKTLLDPChassisID, optixPKTLLDPPortDescription=optixPKTLLDPPortDescription, optixPKTLLDPManagementVID=optixPKTLLDPManagementVID, optixLldpGroupType=optixLldpGroupType, optixPKTLLDPBaseStationInfoEntry=optixPKTLLDPBaseStationInfoEntry, optixPKTLldpNeigheorInfo=optixPKTLldpNeigheorInfo, optixPktLLDPNEGroup=optixPktLLDPNEGroup, optixPKTLLDPSysMacAddr=optixPKTLLDPSysMacAddr, optixPKTLLDPNeigheorInfoTable=optixPKTLLDPNeigheorInfoTable, optixPKTLLDPSystemName=optixPKTLLDPSystemName, optixLldpBoardId=optixLldpBoardId, optixLldpUnknowTlv=optixLldpUnknowTlv, optixPKTLLDPOperMau=optixPKTLLDPOperMau, optixLldpNeigheorInfoBoardId=optixLldpNeigheorInfoBoardId, optixPKTLLDPPortVLANID=optixPKTLLDPPortVLANID, optixLldpNeigheorInfoPortId=optixLldpNeigheorInfoPortId, optixPKTLLDPVlanID=optixPKTLLDPVlanID, optixLldpNeigheorInfoNum=optixLldpNeigheorInfoNum, optixLldpPortId=optixLldpPortId, optixLldpLostTlv=optixLldpLostTlv, optixLldpSendMsg=optixLldpSendMsg, optixPktLLDP=optixPktLLDP, optixLldpAgeNeighbor=optixLldpAgeNeighbor, optixPKTLLDPEntry=optixPKTLLDPEntry, optixLldpTTLMilt=optixLldpTTLMilt, optixLldpVlanPri=optixLldpVlanPri, optixPktLLDPGroup=optixPktLLDPGroup, optixPKTLLDPPortID=optixPKTLLDPPortID, optixLldpLostMsg=optixLldpLostMsg, optixPKTLLDPOMIP=optixPKTLLDPOMIP, optixPKTLLDPNeigheorInfoEntry=optixPKTLLDPNeigheorInfoEntry, optixLldpPerReceiveMsg=optixLldpPerReceiveMsg, optixPKTLLDPNeigheorInfoIndex=optixPKTLLDPNeigheorInfoIndex, optixLldpVlanId=optixLldpVlanId, optixLldpNeigheorInfoSubCardId=optixLldpNeigheorInfoSubCardId, optixPKTLLDPOMMAC=optixPKTLLDPOMMAC, optixLldpWorkModle=optixLldpWorkModle, optixPKTLLDPTable=optixPKTLLDPTable, optixPKTLLDPMTU=optixPKTLLDPMTU, optixPKTLLDPPortAndProtocolVLANID=optixPKTLLDPPortAndProtocolVLANID, optixLldpResetDelay=optixLldpResetDelay, optixPKTLLDPMACPHYConfigurationStatus=optixPKTLLDPMACPHYConfigurationStatus, optixLldpSendInterval=optixLldpSendInterval, optixPKTLLDPManagementAddress=optixPKTLLDPManagementAddress, optixLldpClrstatistic=optixLldpClrstatistic, optixPKTLLDPSystemDescription=optixPKTLLDPSystemDescription, optixLldpNeigheorInfoType=optixLldpNeigheorInfoType)
