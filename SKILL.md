---
name: thsrc
description: Query Taiwan High-Speed Rail (THSRC) information including timetables, live schedules, train status, and seat availability. Use this skill when users ask about Taiwan high-speed rail schedules, train times, station information, or ticket availability in Chinese or English.
---

# Taiwan High-Speed Rail Query Tool

## Overview

Provide real-time Taiwan High-Speed Rail (台湾高铁) information through the TDX (Transport Data Exchange) API. Support queries for timetables, live schedules, specific train information, and seat availability across all 12 THSR stations.

## When to Use This Skill

Activate this skill when users request:
- Taiwan high-speed rail schedules or timetables
- Current train status at specific stations
- Specific train number information
- Seat availability for routes
- THSR station information
- Queries mentioning "高铁", "THSR", "台湾高铁", or station names like "台北", "左营", etc.

## Prerequisites

Ensure TDX API credentials are configured:
- `TDX_CLIENT_ID`: Client ID from TDX platform
- `TDX_CLIENT_SECRET`: Client Secret from TDX platform

Users can obtain credentials at: https://tdx.transportdata.tw/

## Core Capabilities

### 1. Station Information Query

Retrieve all THSR station details including names, IDs, and locations.

**Usage:**
```bash
cd scripts
python thsrc_api.py stations
```

**When to use:** User asks about available stations, station codes, or general THSR network information.

**Reference:** See `references/stations.md` for complete station mapping (Chinese names, English names, station IDs).

### 2. Timetable Query

Query scheduled train times between two stations for a specific date.

**Usage:**
```bash
python thsrc_api.py timetable <origin> <destination> <date>
```

**Parameters:**
- `origin`: Origin station (supports Chinese name, English name, or ID)
- `destination`: Destination station (supports Chinese name, English name, or ID)
- `date`: Travel date in YYYY-MM-DD format

**Examples:**
```bash
# Using Chinese names
python thsrc_api.py timetable 台北 左营 2024-01-15

# Using English names
python thsrc_api.py timetable Taipei Zuoying 2024-01-15

# Using station IDs
python thsrc_api.py timetable 1000 1070 2024-01-15
```

**When to use:** User asks about train schedules between stations for a specific date.

### 3. Live Schedule Query

Get real-time train status at a specific station.

**Usage:**
```bash
python thsrc_api.py live <station>
```

**Parameters:**
- `station`: Station name or ID

**Examples:**
```bash
python thsrc_api.py live 台北
python thsrc_api.py live Taichung
python thsrc_api.py live 1040
```

**When to use:** User asks about current trains, real-time status, or "what trains are at [station] now?"

### 4. Specific Train Information

Query detailed information for a specific train number.

**Usage:**
```bash
python thsrc_api.py train <train_no> <date>
```

**Parameters:**
- `train_no`: Train number (e.g., 823, 1234)
- `date`: Travel date in YYYY-MM-DD format

**Example:**
```bash
python thsrc_api.py train 823 2024-01-15
```

**When to use:** User mentions a specific train number and wants details.

### 5. Seat Availability Query

Check available seats for trains between two stations.

**Usage:**
```bash
python thsrc_api.py seats <origin> <destination> <date>
```

**Parameters:**
- `origin`: Origin station
- `destination`: Destination station
- `date`: Travel date in YYYY-MM-DD format

**Example:**
```bash
python thsrc_api.py seats 台北 高雄 2024-01-15
```

**When to use:** User asks about seat availability, ticket availability, or "are there seats available?"

**Update frequency:**
- Same-day queries: Updated every 10 minutes
- Future dates: Updated at 10:00, 16:00, 22:00 daily

## Implementation Workflow

1. **Parse user request** - Identify query type (timetable, live, seats, etc.)
2. **Extract parameters** - Get station names, dates, train numbers from user input
3. **Normalize station names** - Convert Chinese/English names to station IDs using `references/stations.md` mapping
4. **Execute query** - Run appropriate command from `scripts/thsrc_api.py`
5. **Format response** - Present results in clear, user-friendly format

## Station Name Handling

Support three formats for station input:
- **Chinese names**: 台北, 左营, 台中 (most common)
- **English names**: Taipei, Zuoying, Taichung
- **Station IDs**: 1000, 1070, 1040

**Aliases:**
- 高雄 = 左营 (both refer to station ID 1070)

Load `references/stations.md` when station mapping is needed.

## Date Format Requirements

All dates must follow `YYYY-MM-DD` format (e.g., 2024-01-15).

Convert natural language dates:
- "明天" (tomorrow) → Calculate tomorrow's date
- "下周一" (next Monday) → Calculate date
- "1/15" → Convert to 2024-01-15

## Error Handling

Common errors and solutions:

**Invalid station name:**
- Check against station list in `references/stations.md`
- Suggest correct station names to user

**Missing credentials:**
- Verify TDX_CLIENT_ID and TDX_CLIENT_SECRET environment variables are set
- Guide user to obtain credentials at https://tdx.transportdata.tw/

**Date format error:**
- Ensure date is in YYYY-MM-DD format
- Validate date is not in the past for timetable queries

**API timeout:**
- Retry request once
- Check network connectivity
- Verify TDX API service status

## Response Formatting

Present results clearly:
- **Timetable queries**: Show departure/arrival times, train numbers, travel duration
- **Live schedules**: Display current status, delays, platform information
- **Seat availability**: Indicate available/sold out for each train, seat types
- **Train information**: Show complete route, stops, times

Always include:
- Query parameters used
- Number of results found
- Relevant disclaimers (real-time data accuracy, booking instructions)

## Resources

### scripts/thsrc_api.py
Python script providing TDX API interface. Contains `THSRAPIClient` class with methods for all query types. Execute directly for command-line queries or import for programmatic access.

### references/stations.md
Complete station reference including Chinese names, English names, station IDs, and mapping dictionaries. Load when station name conversion is needed.
