# port-channel-interfaces

# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Name Servers](#name-servers)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)
  - [Management SSH](#management-ssh)
  - [Management GNMI](#management-api-gnmi)
  - [Management API](#Management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [RADIUS Servers](#radius-servers)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
- [Aliases](#aliases)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [SFlow](#sflow)
  - [Hardware Counters](#hardware-counters)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
- [MLAG](#mlag)
- [Spanning Tree](#spanning-tree)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
- [VLANs](#vlans)
- [Interfaces](#interfaces)
  - [Interface Defaults](#interface-defaults)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [Router PIM Sparse Mode](#router-pim-sparse-mode)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
  - [IP Extended Communities](#ip-extended-communities)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [VRF Instances](#vrf-instances)
- [Virtual Source NAT](#virtual-source-nat)
- [Platform](#platform)
- [Router L2 VPN](#router-l2-vpn)
- [IP DHCP Relay](#ip-dhcp-relay)
- [Errdisable](#errdisable)
- [MAC security](#mac-security)
- [QOS](#qos)
- [QOS Profiles](#qos-profiles)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 10.73.255.122/24 | 10.73.255.2 |

#### IPv6

| Management Interface | description | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | --- | ------------ | ------------ |
| Management1 | oob_management | MGMT | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

## DNS Domain

DNS domain not defined

## Domain-list

Domain-list not defined

## Name Servers

No name servers defined

## Domain Lookup

DNS domain lookup not defined

## NTP

No NTP servers defined

## PTP

PTP is not defined.

## Management SSH

Management SSH not defined

## Management API GNMI

Management API gnmi is not defined

## Management API HTTP

Management API HTTP not defined

# Authentication

## Local Users

No users defined

## Enable Password

Enable password not defined

## TACACS Servers

TACACS servers not defined

## IP TACACS Source Interfaces

IP TACACS source interfaces not defined

## RADIUS Servers

RADIUS servers not defined

## AAA Server Groups

AAA server groups not defined

## AAA Authentication

AAA authentication not defined

## AAA Authorization

AAA authorization not defined

## AAA Accounting

AAA accounting not defined

# Management Security

Management security not defined

# Aliases

Aliases not defined

# Monitoring

## TerminAttr Daemon

TerminAttr daemon not defined

## Logging

No logging settings defined

## SNMP

No SNMP settings defined

## SFlow

No sFlow defined

## Hardware Counters

No hardware counters defined

## VM Tracer Sessions

No VM tracer sessions defined

## Event Handler

No event handler defined

# MLAG

MLAG not defined

# Spanning Tree

Spanning-tree not defined

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

**Default Allocation Policy**

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 4094 |

# VLANs

No VLANs defined

# Interfaces

## Interface Defaults

No Interface Defaults defined

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 3 |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet50 | SRV-POD03_Eth1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
!
interface Ethernet50
   description SRV-POD03_Eth1
   channel-group 5 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel5 | DC1_L2LEAF1_Po1 | switched | trunk | 110,201 | - | - | - | - | 5 | - |
| Port-Channel50 | SRV-POD03_PortChanne1 | switched | trunk | 1-4000 | - | - | - | - | - | 0000:0000:0303:0202:0101 |
| Port-Channel51 | ipv6_prefix | switched | trunk | 1-500 | - | - | - | - | - | - |
| Port-Channel100.101 | IFL for TENANT01 | switched | access | - | - | - | - | - | - | - |
| Port-Channel100.102 | IFL for TENANT02 | switched | access | - | - | - | - | - | - | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   switchport
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   mlag 5
   storm-control broadcast level 1
   storm-control multicast level 1
   storm-control unknown-unicast level 1
!
interface Port-Channel50
   description SRV-POD03_PortChanne1
   switchport
   switchport trunk allowed vlan 1-4000
   switchport mode trunk
   !
    evpn ethernet-segment
       identifier 0000:0000:0303:0202:0101
       route-target import 03:03:02:02:01:01
   !
   lacp system-id 0303.0202.0101
!
interface Port-Channel51
   description ipv6_prefix
   switchport
   switchport trunk allowed vlan 1-500
   switchport mode trunk
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
!
interface Port-Channel100
   logging event link-status
   no switchport
!
interface Port-Channel100.101
   description IFL for TENANT01
   logging event link-status
   mtu 1500
   switchport
   ip address 10.1.1.3/31
!
interface Port-Channel100.102
   description IFL for TENANT02
   mtu 1500
   switchport
   vrf C2
   ip address 10.1.2.3/31
```

## Loopback Interfaces

No loopback interfaces defined

## VLAN Interfaces

No VLAN interfaces defined

## VXLAN Interface

No VXLAN interfaces defined

# Routing

## Virtual Router MAC Address

IP virtual router MAC address not defined

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false|
### IP Routing Device Configuration

```eos
```

## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |

## Static Routes

Static routes not defined

## IPv6 Static Routes

IPv6 static routes not defined

## ARP

Global ARP timeout not defined.

## Router OSPF

Router OSPF not defined

## Router ISIS

Router ISIS not defined

## Router BGP

Router BGP not defined

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

*No device configuration required - default values

# Multicast

## IP IGMP Snooping

No IP IGMP configuration

## Router Multicast

Routing multicast not defined

## Router PIM Sparse Mode

Router PIM sparse mode not defined

# Filters

## Community-lists

Community-lists not defined

## Peer Filters

No peer filters defined

## Prefix-lists

Prefix-lists not defined

## IPv6 Prefix-lists

IPv6 prefix-lists not defined

## Route-maps

No route-maps defined

## IP Extended Communities

No extended community defined

# ACL

## Standard Access-lists

Standard access-lists not defined

## Extended Access-lists

Extended access-lists not defined

## IPv6 Standard Access-lists

IPv6 standard access-lists not defined

## IPv6 Extended Access-lists

IPv6 extended access-lists not defined

# VRF Instances

No VRF instances defined

# Virtual Source NAT

Virtual source NAT not defined

# Platform

No platform parameters defined

# Router L2 VPN

Router L2 VPN not defined

# IP DHCP Relay

IP DHCP relay not defined

# Errdisable

Errdisable is not defined.

# MACsec

MACsec not defined

# QOS

QOS is not defined.

# QOS Profiles

QOS Profiles are not defined

# Custom Templates

No custom templates defined
