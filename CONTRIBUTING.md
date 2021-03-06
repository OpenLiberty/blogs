# Signing off your work when contributing a blog post to Open Liberty

If you'd like to write a blog post for OpenLiberty.io, see [README](./README.md) for instructions.

When you contribute to the Open Liberty blog, if you are not employed by IBM, please sign off your work using the standard developer certificate. The sign-off is a line at the end of the commit message that certifies that you wrote it or otherwise have the right to pass it on as an open source patch.

The rules are simple: if you can certify the following information (from link:https://developercertificate.org/[developercertificate.org]):

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
660 York Street, Suite 102,
San Francisco, CA 94110 USA

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

...add a line to end of the Git commit message:

```
Signed-off-by: Jane Williams <jane.williams@email.com>
```

Use your real name. Sorry, no pseudonyms or anonymous contributions.

Many Git UI tools have support for adding the `Signed-off-by` line to the end of your commit message. This line can be automatically added by the `git commit` command by using the `-s` option.

Thanks to link:https://github.com/bndtools/bnd/blob/master/CONTRIBUTING.md[Bndtools] for the wording on this sign-off process.
