# Lanyard Card Visual Reference

## Component Preview

```
                    |
                    | ← Lanyard strap (gradient purple/indigo)
                    |
              _______________
             /               \
            |  ┌─────┐       |
            |  │  S  │       | ← Logo circle
            |  └─────┘       |
            |                |
            | HELLO,         | ← Label text
            | JOHN DOE       | ← User's name (bold, caps)
            |                |
            |   ~ ~ ~        | ← Pattern decoration
            |________________|
                  ↑
            Purple gradient card
            with glass effect


## Layout Structure

┌─────────────── NAVBAR ───────────────┐
│  SkillSet AI    [Links]    [Avatar]  │
└──────────────────────────────────────┘
                  ║  ← Strap attached
                  ║
              ╔════════╗
              ║ HELLO, ║  ← Lanyard Card
              ║  USER  ║
              ╚════════╝

┌──────────────────────────────────────┐
│  Welcome back, User! 👋               │  ← Welcome Section
│  Here's your learning progress...    │
└──────────────────────────────────────┘
```

## Color Scheme

### Light Mode
- **Card Background:** Linear gradient
  - Start: #667eea (Soft purple)
  - End: #764ba2 (Deep purple)
- **Strap:** #6366f1 (Indigo)
- **Text:** White with shadow
- **Logo Circle:** White with opacity

### Dark Mode
- **Card Background:** Linear gradient
  - Start: #4c1d95 (Dark purple)
  - End: #5b21b6 (Deep purple)
- **Strap:** #8b5cf6 (Purple)
- **Text:** White with shadow
- **Logo Circle:** White with opacity

## Interactive Features

```
Mouse Position: (x, y)
        ↓
   Card tilts in 3D
        ↓
┌─────────────┐        ┌──────────────┐
│   Normal    │   →    │   Tilted     │
│   Position  │  hover │   (follows   │
└─────────────┘        │    mouse)    │
                       └──────────────┘
```

## Responsive Sizes

| Screen Size | Card Size    | Font Size |
|-------------|--------------|-----------|
| Desktop     | 280 × 180 px | 28px      |
| Tablet      | 240 × 160 px | 24px      |
| Mobile      | 200 × 140 px | 20px      |

## Animation Flow

```
Page Load
    ↓
Lanyard appears
    ↓
User moves mouse
    ↓
Card tilts smoothly (3D)
    ↓
User hovers card
    ↓
Cursor → "grab"
    ↓
User clicks & drags
    ↓
Cursor → "grabbing"
```

## Text Display Logic

```javascript
if (user.displayName exists)
    show displayName.toUpperCase()
else if (user.email exists)
    show email.split('@')[0].toUpperCase()
else
    show "USER"
```

## Examples

### Example 1: Full Name
```
┌─────────────────┐
│  HELLO,         │
│  JOHN SMITH     │
└─────────────────┘
```

### Example 2: Email Username
```
┌─────────────────┐
│  HELLO,         │
│  JOHNDOE123     │
└─────────────────┘
```

### Example 3: Fallback
```
┌─────────────────┐
│  HELLO,         │
│  USER           │
└─────────────────┘
```

## CSS Transform Details

```css
/* 3D Transform Applied on Mouse Move */
transform: 
    perspective(1000px)      /* Creates depth */
    rotateY(Xdeg)           /* Horizontal tilt */
    rotateX(-Ydeg)          /* Vertical tilt */
    translateY(10px);       /* Slight downward offset */

/* Smooth Transition */
transition: transform 0.1s ease-out;
```

## Shadow & Depth

```
Outer Shadow (Glow):
├─ Blur: 60px
├─ Spread: -15px
└─ Color: rgba(102, 126, 234, 0.5)

Inner Border:
├─ Width: 1px
└─ Color: rgba(255, 255, 255, 0.1)

Text Shadow:
├─ Offset: 0 2px
├─ Blur: 8px
└─ Color: rgba(0, 0, 0, 0.3)
```

## Z-Index Layering

```
┌─ Layer 1 (z-1): Background pattern
│
├─ Layer 2 (z-0): Card base
│
├─ Layer 3 (z-1): Lanyard strap
│
└─ Layer 4 (z-2): Card content (text)
```
