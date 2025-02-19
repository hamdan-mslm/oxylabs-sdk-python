# Contributing

Thanks for taking the time to contribute!

All types of contributions are encouraged and valued. Please try to read the
relevant sections in this document before making your contribution. It will
make it a lot easier for us maintainers and smooth out the experience for all
involved. The community looks forward to your contributions.

> And if you like the project, but just don't have time to contribute, that's
> fine. There are other easy ways to support the project and show your
> appreciation, which we would also be very happy about:
> - Star the project
> - Post about it on social media
> - Refer this project in your own project's README
> - Mention the project at local meetups and tell your friends/colleagues

## I Have a Question

> Please ensure you've already read the available
> [Documentation](https://developers.oxylabs.io/), which may have
> answered your question.

Before you ask a question, it is best to search for existing
[Issues](https://github.com/mslmio/oxylabs-sdk-python/issues) that might help 
you. In case you have found a suitable issue and still need clarification, you 
can write your question in this issue. It is also advisable to search the 
internet for answers first.

If you then still feel the need to ask a question and need clarification, we
recommend the following:

- Open an [Issue](https://github.com/mslmio/oxylabs-sdk-python/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what
  seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

> ### Legal Notice
>
> When contributing to this project, you must agree that you have authored 100%
> of the content, that you have the necessary rights to the content and that
> the content you contribute may be provided under the project licence.

## Code Formatting

This project uses [Black](https://black.readthedocs.io/en/stable/) and 
[isort](https://pycqa.github.io/isort/) for code formatting. Before you submit 
your contribution, please make sure your code is formatted according to these 
style guides.

First, you will need to install the required tools if you haven't already:

```bash
pip install black isort
```

You can use the provided `fmt.sh` script to automatically format your code. 
This script runs `isort` and `black` on the `src` directory. Here's how you can 
run it:

```bash
scripts/fmt.sh
```

## Running Tests

To ensure the quality of the code, we encourage you to run tests after making 
any changes and before submitting a contribution. We have a script that 
facilitates running the unit tests for the project.

To run the tests, use the `tests.sh` script located in the `scripts` directory.
This will execute all the unit tests and report any failures.

Here's how you can run it:

```bash
scripts/tests.sh
```

### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more
information. Therefore, we ask you to investigate carefully, collect
information and describe the issue in detail in your report. Please complete
the following steps in advance to help us fix any potential bug as fast as
possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g.
  using incompatible environment components/versions (Make sure that you have
  read the
  [documentation](https://developers.oxylabs.io/). If you
  are looking for support, you might want to check [this
  section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the
  same issue you are having, check if there is not already a bug report
  existing for your bug or error in the [bug
  tracker](https://github.com/mslmio/oxylabs-sdk-python/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if
  users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package
  manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with
  older versions?

#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs
> including sensitive information to the issue tracker, or elsewhere in public.
> Instead sensitive bugs must be sent by email to .

We use GitHub issues to track bugs and errors. If you run into an issue with the
project:

- Open an [Issue](https://github.com/mslmio/oxylabs-sdk-python/issues/new).
  (Since we can't be sure at this point whether it is a bug or not, we ask you 
  not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction
  steps* that someone else can follow to recreate the issue on their own. This
  usually includes your code. For good bug reports you should isolate the
  problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If
  there are no reproduction steps or no obvious way to reproduce the issue, the
  team will ask you for those steps and mark the issue as `needs-repro`. Bugs
  with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as
  well as possibly other tags (such as `critical`), and the issue will be left
  to be [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion,
**including completely new features and minor improvements to existing
functionality**. Following these guidelines will help maintainers and the
community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://developers.oxylabs.io/) carefully and
  find out if the functionality is already covered, maybe by an individual
  configuration.
- Perform a [search](https://github.com/mslmio/oxylabs-sdk-python/issues) to see
  if the enhancement has already been suggested. If it has, add a comment to the
  existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's
  up to you to make a strong case to convince the project's developers of the
  merits of this feature. Keep in mind that we want features that will be
  useful to the majority of our users and not just a small subset. If you're
  just targeting a minority of users, consider writing an add-on/plugin
  library.

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as
[GitHub issues](https://github.com/mslmio/oxylabs-sdk-python/issues).

- Use a **clear and descriptive title** for the issue to identify the
  suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as
  many details as possible.
- **Describe the current behavior** and **explain which behavior you expected
  to see instead** and why. At this point you can also tell which alternatives
  do not work for you.
- You may want to **include screenshots or screen recordings** which help you
  demonstrate the steps or point out the part which the suggestion is related
  to.
- **Explain why this enhancement would be useful** to most users. You may also
  want to point out the other projects that solved it better and which could
  serve as inspiration.

## Security Issue Notifications

Please see Oxylabs' [Vulnerability Disclosure
Policy](https://oxylabs.io/legal/vulnerability-disclosure-policy) for details.
