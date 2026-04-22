---
name: numerical-stat-core
description: 一个用于数值计算与属性推导的核心 TypeScript 库。处理权重计算、增长曲线和各种数值推算逻辑。
---

# Numerical Stat Core

用于处理复杂数值增长和属性计算的数学核心引擎。

## Requirements
- TypeScript
- No external runtime dependencies

## Usage

1. Copy `resources/types.ts` and `resources/calculator.ts` to your project (e.g., `lib/rpg/`).

2. Initialize the engine with your game's specific configuration:

```typescript
import { RPGEngine } from '@/lib/rpg/calculator';

// 1. Define your game rules
const DevilHunterConfig = {
    baseHP: 100,
    hpPerLevel: 2,
    pointsPerLevel: 5,
    validAttributes: ['STR', 'CON', 'TEC', 'INT'],
    attributeMultipliers: {
        'CON': 5, // 1 CON = 5 HP
        'STR': 0,
    }
};

const engine = new RPGEngine(DevilHunterConfig);

// 2. Use it in your UI components
const level = 50;
const availablePoints = engine.calculateAvailablePoints(level);
const maxHP = engine.calculateMaxHP(level, 100, 'CON'); // Level 50, 100 CON

console.log(`At level ${level}, you have ${availablePoints} points.`);
console.log(`Max HP: ${maxHP}`);
```

## Extending
For complex logic (like "Innate Talents" or "Hybrid Multipliers"), extend the `RPGEngine` class:

```typescript
class AdvancedEngine extends RPGEngine {
    calculateStats(stats: CharacterStats) {
        // ... custom logic ...
    }
}
```
