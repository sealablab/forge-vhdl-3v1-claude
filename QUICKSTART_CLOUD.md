# VHDL-FORGE Cloud Quick Start

**Get started with VHDL development in Claude Code Web in under 3 minutes!**

---

## Step 1: Open in Claude Code Web

If you're reading this, you're probably already here! If not:

1. Go to [Claude Code](https://claude.ai/code)
2. Clone this repository
3. Continue to Step 2

---

## Step 2: Run Setup (One Command!)

Copy and paste this into the terminal:

```bash
uv run python scripts/cloud_setup_with_ghdl.py
```

**This will:**
- ✅ Install GHDL (VHDL simulator)
- ✅ Set up Python environment
- ✅ Install all dependencies
- ✅ Run a sample test to verify everything works
- ⏱️ Takes about 2-3 minutes

**Wait for:** "Setup Complete!" message

---

## Step 3: Verify It Works

List available tests:

```bash
uv run python cocotb_tests/run.py --list
```

Run a simple test:

```bash
uv run python cocotb_tests/run.py forge_util_clk_divider
```

**You should see:** Test passes with ~10-15 lines of output

---

## Step 4: Start Developing!

You now have a full VHDL development environment in your browser!

**Try these commands:**

```bash
# Start requirements gathering for a new component
/gather-requirements

# Run all tests (P1 level - fast)
uv run python cocotb_tests/run.py --all

# Explore example components
ls vhdl/components/

# Check out the counter example
cd examples/counter && cat README.md
```

---

## What Just Happened?

You now have:
- ✅ GHDL VHDL simulator
- ✅ CocoTB testing framework
- ✅ All FORGE VHDL utilities
- ✅ AI-assisted development agents
- ✅ Progressive testing infrastructure

All running in your browser. No local installation required!

---

## Next Steps

1. **Learn the patterns:**
   - Read `README.md` - Overview and key features
   - Read `CLAUDE.md` - Complete development guide
   - Read `llms.txt` - Quick reference

2. **Explore examples:**
   - `examples/counter/` - Complete 3-layer FORGE example
   - `vhdl/components/` - Reusable VHDL components

3. **Create your own component:**
   - Type `/gather-requirements` to start
   - Follow the 7-phase guided process
   - Let the AI agents generate VHDL + tests

4. **Test everything:**
   - Run tests: `uv run python cocotb_tests/run.py <component>`
   - P1 tests are fast (<5 seconds, <20 line output)
   - Perfect for AI-assisted iteration!

---

## Troubleshooting

**Setup failed?**
- Check `docs/CLOUD_SETUP_PROMPT.md` for detailed guide
- See `docs/diagnostic_reports/` for known issues

**Tests not working?**
- Run validation: `./scripts/validate_setup.sh`
- Check GHDL: `ghdl --version` (should show 4.0+)

**Need help?**
- Full documentation in `docs/`
- AI agent workflows in `.claude/`
- Ask Claude Code for guidance!

---

**Welcome to cloud-first VHDL development!** 🚀
