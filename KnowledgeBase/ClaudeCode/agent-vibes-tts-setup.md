# 🔧 AgentVibes – Text-to-Speech for AI Coding Agents

## Purpose of This Document
This document covers how to set up and configure AgentVibes, a Text-to-Speech (TTS) tool that gives voice feedback to AI coding agent sessions. Voice output adds a secondary feedback channel during AI-assisted development, making it easier to follow agent progress without constantly watching the terminal. This is relevant to any project using Claude Code as part of an AI-assisted mobile development workflow.

---

## 1. What AgentVibes Does

AgentVibes adds spoken audio feedback to Claude Code sessions. It hooks into session lifecycle events and reads out key agent actions, decisions, and results.

> **Voice feedback lets you multitask — follow agent progress by ear while reviewing code, testing, or working in another tool.**

### 1.1 Key Capabilities
- Speaks agent output during Claude Code sessions
- Configurable verbosity (how much gets spoken)
- Adjustable voice, speed, and provider
- Installs entirely into the `.claude/` directory — no global dependencies

---

## 2. Setup

### 2.1 Prerequisites
- Claude Code CLI installed
- Node.js / npm available (for `npx`)
- macOS (for macOS Say provider) or Linux (for Piper provider)

### 2.2 Installation

Run from your project root:

```bash
npx agent-vibes init
```

This installs into `.claude/`:
- `hooks/` — TTS scripts (play-tts.sh, voice-manager.sh, etc.)
- `commands/agent-vibes/` — Slash commands
- `config/` — Audio and music configuration
- `settings.json` — Session start hook registration

### 2.3 Verify Installation

Start a new Claude Code session. You should hear a voice greeting. If not, check that `.claude/settings.json` contains the `SessionStart` hook and test manually with:

```bash
.claude/hooks/play-tts.sh "test"
```

---

## 3. Configuration

### 3.1 Voice

On macOS, use any installed system voice. List available voices with `say -v '?'`.

Set voice via slash command:
```
/agent-vibes:switch <voice-name>
```

✅ **Recommended macOS voices**: Zoe (Premium), Samantha (default, reliable), Daniel (British English)

### 3.2 Speed

```
/agent-vibes:set-speed <value>
```

| Value | Effect |
|-------|--------|
| `0.5x` | Half speed (slower) |
| `normal` / `1x` | Normal speed |
| `2x` | Double speed |
| `3x` | Triple speed |

### 3.3 Verbosity

Controls how much the agent speaks during work:

```
/agent-vibes:verbosity <level>
```

| Level | What gets spoken |
|-------|-----------------|
| `low` | Action acknowledgment + final result only |
| `medium` | Above + key decisions |
| `high` | Above + full reasoning and trade-offs |

✅ **Start with `high` to understand what the agent is doing, then dial back to `medium` or `low` once comfortable**

### 3.4 TTS Provider

| Provider | Platform | Notes |
|----------|----------|-------|
| `macos` | macOS | Uses built-in `say` command, zero setup |
| `piper` | Any | Open-source neural TTS, requires install |

```
/agent-vibes:provider list
/agent-vibes:provider switch <name>
```

---

## 4. Recommended Defaults

For most mobile development projects, this is a solid starting configuration:

```bash
echo "Zoe" > .claude/tts-voice.txt
echo "macos" > .claude/tts-provider.txt
echo "high" > .claude/tts-verbosity.txt
echo "1.0" > .claude/config/tts-speech-rate.txt
```

---

## 5. Common Slash Commands

| Command | Description |
|---------|-------------|
| `/agent-vibes:switch <voice>` | Change voice |
| `/agent-vibes:set-speed <speed>` | Adjust speech rate |
| `/agent-vibes:verbosity <level>` | Set verbosity |
| `/agent-vibes:mute` / `unmute` | Toggle TTS output |
| `/agent-vibes:preview` | Preview available voices |
| `/agent-vibes:whoami` | Show current voice and provider |
| `/agent-vibes:update` | Update to latest version |
| `/agent-vibes:clean` | Clean TTS audio cache |

---

## 6. Git Considerations

TTS config is a personal preference. Add to `.gitignore` if not sharing with the team:

```gitignore
.claude/tts-voice.txt
.claude/tts-provider.txt
.claude/tts-verbosity.txt
.claude/config/tts-speech-rate.txt
.claude/audio/
```

✅ **Commit these files if you want a shared team setup**
❌ **Don't commit if each developer should choose their own voice/speed preferences**

---

## 7. Troubleshooting

| Problem | Fix |
|---------|-----|
| No sound on session start | Check `.claude/settings.json` has the SessionStart hook; run `.claude/hooks/play-tts.sh "test"` manually |
| Voice not found | Run `say -v '?'` to list installed voices; download more in System Settings > Accessibility > Spoken Content |
| Speed not changing | Verify `.claude/config/tts-speech-rate.txt` value; restart Claude Code session |

---

## 8. Summary

1. **AgentVibes adds voice feedback to Claude Code sessions**, providing an audio channel for agent progress
2. **Install with `npx agent-vibes init`** — everything lives in `.claude/`, no global setup
3. **Configure voice, speed, verbosity, and provider** to match your workflow preference
4. **Start with high verbosity** and dial back as you get comfortable with the tool
5. **Git-ignore personal preferences** or commit for shared team configuration
