---
title: "OpenAI Codex Tips & Tricks: Listing Available Models"
date: 2025-04-19T09:00:00+10:00
draft: false
description: "Useful techniques for working efficiently with OpenAI's Codex CLI tool"
author: "david-taylor"
tags: ["OpenAI", "Codex", "CLI", "AI", "Development Tools", "Tips"]
categories: ["Tutorials"]
series: ["OpenAI Codex Tips & Tricks"]
---

After [getting started with OpenAI Codex CLI](/posts/2025-04-17-getting-started-with-openai-codex-cli/), I've discovered some handy tips to make working with it a bit easier.

## Listing Available Models

When working with Codex CLI, you can specify which model to use with the `-m` flag:

```bash
codex -m o4-mini "explain this code"
```

But what if you want to know all the models available to you? The default documentation doesn't provide a straightforward way to list them. Here's a simple one-liner that queries the OpenAI API to list all models available to your account:

```bash
curl -s -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models | \
  python3 -c "import sys,json; \
  data=json.load(sys.stdin)['data']; \
  print('\n'.join(item['id'] for item in data))"
```

This command:
1. Makes an authenticated request to the OpenAI API
2. Gets the full list of models
3. Extracts and prints just the model IDs in a list

The output will include **all** models your API key has access to - as far as I can tell, there's no easy way to identify which of those models work well with Codex.

## Filtering and Sorting Model Results

The raw output from the API includes all models in your account, including date-stamped versions. For a cleaner list, you could filter and sort the results.

If you have `jq` installed, this command gives a clean, sorted list without date-stamped model versions:

```bash
curl -s -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models | \
  jq -r '.data[].id' | \
  grep -Ev '[0-9]{4}-[0-9]{2}-[0-9]{2}' | \
  sort -u
```

Using this command, you'll see models like:

```
babbage-002
chatgpt-4o-latest
gpt-3.5-turbo
gpt-4
gpt-4.1
gpt-4o
o1
o1-mini
o1-preview
o1-pro
o3-mini
o4-mini
```

For Codex CLI, the default model is `o4-mini`, which works well for most coding tasks, offering a good balance of speed and capability. However, you might notice there's no `o3` in the list...

## Missing Models?

If you run the commands above but don't see certain models (like `o3`), or if you encounter errors about streaming responses, you likely need to complete organisation verification with OpenAI.

The [Codex README](https://github.com/openai/codex/blob/main/README.md) specifically notes: "It's possible that your API account needs to be verified in order to start streaming responses with models like o3 or o4-mini." According to the [official verification documentation](https://help.openai.com/en/articles/10910291-api-organization-verification), this additional step is required for certain API features and models. I suspect this requirement came about following speculation that DeepSeek's model was trained using the OpenAI API.

The verification process requires you to provide identifying information and biometric data. It involves:

1. Logging into the OpenAI Platform
2. Going to [Organization Settings](https://platform.openai.com/settings/organization/general)
3. Clicking "Verify Organization"

![OpenAI Verify Organization button](/images/2025/04/screenshot_openai_verify_organization.png)

4. Completing an identity verification process that includes providing ID documentation

![OpenAI Identity Verification](/images/2025/04/screenshot_openai_verify_identity.png)

5. Completing biometric (face) verification through a third-party service called Persona

![OpenAI Verify with Persona](/images/2025/04/screenshot_openai_verify_with_persona.png)

6. Waiting for the verification to be processed and approved

![OpenAI Verification Complete](/images/2025/04/screenshot_openai_verified.png)

If you're uncomfortable with this verification process, you can still use models that don't require verification, such as the default `o4-mini`.

## Choosing the Right Model

According to the [official documentation](https://github.com/openai/codex/blob/main/README.md), Codex CLI supports "any model available with Responses API" with `o4-mini` set as the default. That doesn't help us choose the best model for a task or project, though. So, I've put together the following simple guide based on OpenAI's documentation and some of my own experimentation:

| Model | Capabilities | Relative Speed | Verification Required? | Notes |
|-------|--------------|----------------|----------|-------|
| o4-mini | Strong STEM and vision performance | Fast | No* | Default choice, optimized for latency and cost |
| o1-mini | General text and code generation | Fastest | No | More economical for simpler tasks |
| o3 | Advanced multimodal reasoning | Medium | Yes | Supports text, code, and image inputs |
| o1 | Advanced text and code generation | Slower | No | More powerful for complex problems |
| o1-pro | Premium capabilities | Slowest | No | Highest capabilities, highest cost |
| GPT-4.1 | Alternative to "o" series | Medium | No | Can be specified with `--model gpt-4.1` |

*While `o4-mini` is generally available, the README says that "your API account needs to be verified in order to start streaming responses" which may affect some functionality.

Model availability and verification requirements will change over time. Also, the official Codex GitHub repo describes the tool as "an experimental project under active development."

The model you choose should depend on your specific task requirements, budget considerations, and performance needs. For most development tasks, the default `o4-mini` provides a decent balance.

## Additional Model Options

While the "o" series models are the ones you're most likely to use with Codex CLI, the README says you can use "any model available with Responses API" by specifying it with the `--model` flag (e.g., `codex --model gpt-4.1`). If you wanted to filter the earlier list of models to only the "o" series, you can modify the command:

```bash
curl -s -H "Authorization: Bearer $OPENAI_API_KEY" \
  https://api.openai.com/v1/models | \
  python3 -c "import sys,json; \
  data=json.load(sys.stdin)['data']; \
  print('\n'.join(item['id'] for item in data if item['id'].startswith('o')))"
```

This filters the results to show only models with IDs starting with 'o' (like o4-mini, o1, etc.).

## Adding the Command to Your Shell Profile

For convenience, you might want to add this as a function in your `.bashrc` or `.zshrc`:

```bash
function list-codex-models() {
  curl -s -H "Authorization: Bearer $OPENAI_API_KEY" \
    https://api.openai.com/v1/models | \
    jq -r '.data[].id' | \
    grep -E '^o' | \
    grep -Ev '[0-9]{4}-[0-9]{2}-[0-9]{2}' | \
    sort -u
}
```

Then you can simply run `list-codex-models` whenever you need to check which models are available.

## Limitations and Caveats

As noted in the [GitHub repository](https://github.com/openai/codex/blob/main/README.md), there are a few important caveats to be aware of:

1. **Experimental status**: The Codex CLI is "an experimental project under active development" which means features and model support may change
  
2. **Zero Data Retention**: If your OpenAI organization has Zero Data Retention (ZDR) enabled, you won't be able to use Codex CLI as it requires the `store:true` parameter

3. **API access**: While the CLI is open-source, you still need an OpenAI API key with appropriate credits and access levels to use it effectively

After I've played with Codex a little more, I'll share more tips and tricks. In the meantime, if you've discovered any useful techniques, I'd love to hear about them!
