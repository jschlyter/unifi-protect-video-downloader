# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- TBD

### Changed
- TBD

### Deprecated
- TBD

### Removed
- TBD

### Fixed
- TBD

### Security
- TBD


## [v2.1.2]
### Fixed
- fix ongoing `MotionEvent`s causing `NoneType` error due to missing `end` time
([#65](https://github.com/danielfernau/unifi-protect-video-downloader/issues/65) by
[@JimReprogle](https://github.com/JimReprogle), and
[#115](https://github.com/danielfernau/unifi-protect-video-downloader/pull/115) by
[@L3o-pold](https://github.com/L3o-pold) via
[#114](https://github.com/danielfernau/unifi-protect-video-downloader/pull/114))

### Security
- bump mypy from 0.940 to 0.941
([#105](https://github.com/danielfernau/unifi-protect-video-downloader/pull/105)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.12 to 2.27.13
([#107](https://github.com/danielfernau/unifi-protect-video-downloader/pull/107)
via [dependabot](https://github.com/apps/dependabot))
- bump pytest from 7.1.0 to 7.1.1
([#108](https://github.com/danielfernau/unifi-protect-video-downloader/pull/108)
via [dependabot](https://github.com/apps/dependabot))
- bump responses from 0.19.0 to 0.20.0
([#109](https://github.com/danielfernau/unifi-protect-video-downloader/pull/109)
via [dependabot](https://github.com/apps/dependabot))
- bump types-python-dateutil from 2.8.9 to 2.8.10
([#110](https://github.com/danielfernau/unifi-protect-video-downloader/pull/110)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.13 to 2.27.14
([#111](https://github.com/danielfernau/unifi-protect-video-downloader/pull/111)
via [dependabot](https://github.com/apps/dependabot))
- bump mypy from 0.941 to 0.942
([#112](https://github.com/danielfernau/unifi-protect-video-downloader/pull/112)
via [dependabot](https://github.com/apps/dependabot))
- bump pylint from 2.12.2 to 2.13.0
([#113](https://github.com/danielfernau/unifi-protect-video-downloader/pull/113)
via [dependabot](https://github.com/apps/dependabot))
- bump pylint from 2.13.0 to 2.13.2
([#116](https://github.com/danielfernau/unifi-protect-video-downloader/pull/116)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.14 to 2.27.15
([#117](https://github.com/danielfernau/unifi-protect-video-downloader/pull/117)
via [dependabot](https://github.com/apps/dependabot))


## [v2.1.1]
### Added
- GitHub Actions: add Docker image tags and automated edge builds from master branch
([#93](https://github.com/danielfernau/unifi-protect-video-downloader/pull/93) by
[@L3o-pold](https://github.com/L3o-pold))
and ([#104](https://github.com/danielfernau/unifi-protect-video-downloader/pull/104) by
[@danielfernau](https://github.com/danielfernau))

### Security
- bump click from 8.0.3 to 8.0.4
([#94](https://github.com/danielfernau/unifi-protect-video-downloader/pull/94)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.10 to 2.27.11
([#95](https://github.com/danielfernau/unifi-protect-video-downloader/pull/95)
via [dependabot](https://github.com/apps/dependabot))
- bump actions/setup-python from 2 to 3
([#97](https://github.com/danielfernau/unifi-protect-video-downloader/pull/97)
via [dependabot](https://github.com/apps/dependabot))
- bump actions/checkout from 2 to 3
([#99](https://github.com/danielfernau/unifi-protect-video-downloader/pull/99)
via [dependabot](https://github.com/apps/dependabot))
- bump responses from 0.18.0 to 0.19.0
([#100](https://github.com/danielfernau/unifi-protect-video-downloader/pull/100)
via [dependabot](https://github.com/apps/dependabot))
- bump pytest from 7.0.1 to 7.1.0
([#101](https://github.com/danielfernau/unifi-protect-video-downloader/pull/101)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.11 to 2.27.12
([#102](https://github.com/danielfernau/unifi-protect-video-downloader/pull/102)
via [dependabot](https://github.com/apps/dependabot))
- bump mypy from 0.931 to 0.940
([#103](https://github.com/danielfernau/unifi-protect-video-downloader/pull/103)
via [dependabot](https://github.com/apps/dependabot))


## [2.1.0] - 2022-02-20
### Added
- GitHub Actions: CodeQL workflow
([#74](https://github.com/danielfernau/unifi-protect-video-downloader/pull/74) by
[@danielfernau](https://github.com/danielfernau))
- GitHub Actions: add dependabot scanner
([#75](https://github.com/danielfernau/unifi-protect-video-downloader/pull/75) by
[@ch3ck](https://github.com/ch3ck))
- add custom port support for protect archiver
([#76](https://github.com/danielfernau/unifi-protect-video-downloader/pull/76) by
[@ch3ck](https://github.com/ch3ck))
- CI: add pre-commit checks
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- add CHANGELOG.md and version history
([000a8bd](https://github.com/danielfernau/unifi-protect-video-downloader/commit/000a8bd11d168dfed5e55e292a7f47466922d5ed) by
[@ch3ck](https://github.com/ch3ck)
and [#91](https://github.com/danielfernau/unifi-protect-video-downloader/pull/91) by
[@danielfernau](https://github.com/danielfernau))
- add mypy checks
([#85](https://github.com/danielfernau/unifi-protect-video-downloader/pull/85) by
[@ch3ck](https://github.com/ch3ck))

### Changed
- update CI Lint checks to support Python 3.8, 3.9 and 3.10
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- refactor code with lint checks and fixes
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- transfer repository back to original GitHub user account
([#86](https://github.com/danielfernau/unifi-protect-video-downloader/pull/86) by
[@danielfernau](https://github.com/danielfernau))

### Fixed
- add missing dependencies in BUILD.md
([#55](https://github.com/danielfernau/unifi-protect-video-downloader/pull/55) by
[@MrStevenFeldman](https://github.com/MrStevenFeldman))
- apply mypy code fixes
([#85](https://github.com/danielfernau/unifi-protect-video-downloader/pull/85) by
[@ch3ck](https://github.com/ch3ck))

### Security
- remove cleartext logging of username
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- update dependencies in pyproject.toml
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- replace `zapier/python:latest` with `python:3` as Docker base image
([#77](https://github.com/danielfernau/unifi-protect-video-downloader/pull/77) by
[@ch3ck](https://github.com/ch3ck))
- bump types-requests from 2.27.8 to 2.27.9
([#87](https://github.com/danielfernau/unifi-protect-video-downloader/pull/87)
via [dependabot](https://github.com/apps/dependabot))
- bump pytest from 7.0.0 to 7.0.1
([#88](https://github.com/danielfernau/unifi-protect-video-downloader/pull/88)
via [dependabot](https://github.com/apps/dependabot))
- bump types-requests from 2.27.9 to 2.27.10
([#90](https://github.com/danielfernau/unifi-protect-video-downloader/pull/90)
via [dependabot](https://github.com/apps/dependabot))


## [2.0.2] - 2021-05-09
### Changed
- improve console output of 'events' command
([#51](https://github.com/danielfernau/unifi-protect-video-downloader/pull/51) by
[@danielfernau](https://github.com/danielfernau))

### Fixed
- fix 'sync' command not working with updated 'ProtectClient'
([#50](https://github.com/danielfernau/unifi-protect-video-downloader/pull/50) by
[@danielfernau](https://github.com/danielfernau))


## [2.0.1] - 2020-05-02
### Added
- add Docker images for linux/arm64
([aecc263](https://github.com/danielfernau/unifi-protect-video-downloader/commit/aecc263174b30f18dbbec34daba7d3aba400c50d) by
[@danielfernau](https://github.com/danielfernau))
- GitHub Actions: add dockerbuild workflow
([#42](https://github.com/danielfernau/unifi-protect-video-downloader/pull/42) by
[@danielfernau](https://github.com/danielfernau))
- add BUILD.md with build instructions and development hints
([054b163](https://github.com/danielfernau/unifi-protect-video-downloader/commit/054b1636a3c4b856100e5be3e37fd2b45af7de50) by
[@danielfernau](https://github.com/danielfernau))
- add support for UniFi OS authentication
([#46](https://github.com/danielfernau/unifi-protect-video-downloader/pull/46) by
[@danielfernau](https://github.com/danielfernau))

### Changed
- bump project's python-version from 3.8.1 to 3.8.2
([233120b](https://github.com/danielfernau/unifi-protect-video-downloader/commit/233120b9dbc914c7d7419dd45b235d5153bb6396) by
[@danielfernau](https://github.com/danielfernau))
- skip motion event download if camera is not available via API
([04f35a9](https://github.com/danielfernau/unifi-protect-video-downloader/commit/04f35a9f63efee70ec9847f57f1630e9daf462e4) by
[@danielfernau](https://github.com/danielfernau))
- update GitHub Actions
([#42](https://github.com/danielfernau/unifi-protect-video-downloader/pull/42) by
[@danielfernau](https://github.com/danielfernau))

### Fixed
- fix Event downloads broken
([#29](https://github.com/danielfernau/unifi-protect-video-downloader/issues/29))
- fix Wiki links in README
([d68f42f](https://github.com/danielfernau/unifi-protect-video-downloader/commit/d68f42fdfde1dcc6829e0f366113937ed8417772) by
[@danielfernau](https://github.com/danielfernau))
- fix 'object is not subscriptable' error in cli/events.py
([b375901](https://github.com/danielfernau/unifi-protect-video-downloader/commit/b375901e99927adbad47ef292113a8ce7f701954) by
[@danielfernau](https://github.com/danielfernau))


## [2.0.0] - 2020-04-06
### Added
- add Docker images for linux/amd64
([#24](https://github.com/danielfernau/unifi-protect-video-downloader/pull/24) by
[@danielfernau](https://github.com/danielfernau))
- add Dockerfile and Makefile
([d5e881b](https://github.com/danielfernau/unifi-protect-video-downloader/commit/d5e881b61b976fd8eea93329fec613483577ed80) by
[@danielfernau](https://github.com/danielfernau))
- add Poetry configuration
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10)
by [@dcramer](https://github.com/dcramer))
- add code formatting rules using Black
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10) by
[@dcramer](https://github.com/dcramer))
- add tests
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10) by
[@dcramer](https://github.com/dcramer))
- add support for Motion events
([#3](https://github.com/danielfernau/unifi-protect-video-downloader/issues/3) by
[@peteytoo](https://github.com/peteytoo) and
[#20](https://github.com/danielfernau/unifi-protect-video-downloader/pull/20) by
[@danielfernau](https://github.com/danielfernau))
- add option to download Motion event Heat Maps
([#20](https://github.com/danielfernau/unifi-protect-video-downloader/pull/20) by
[@danielfernau](https://github.com/danielfernau))
- add `sync` command for resuming downloads "rsync style"
([#5](https://github.com/danielfernau/unifi-protect-video-downloader/issues/5) by
[@purpleidea](https://github.com/purpleidea) and
[#18](https://github.com/danielfernau/unifi-protect-video-downloader/pull/18) by
[@dcramer](https://github.com/dcramer))
- add support for UDM-based installations using
[@Silvenga/unifi-udm-api-proxy](https://github.com/Silvenga/unifi-udm-api-proxy)
([#27](https://github.com/danielfernau/unifi-protect-video-downloader/pull/27) by
[@danielfernau](https://github.com/danielfernau))
- add CI via GitHub Actions
([adff6a8](https://github.com/danielfernau/unifi-protect-video-downloader/commit/adff6a804b30150799875ac33cd5bc83030ca4c5) by
[@dcramer](https://github.com/dcramer))

### Changed
- switch from GPLv3 to MIT License
(as suggested in [#8](https://github.com/danielfernau/unifi-protect-video-downloader/issues/8) by
[@dcramer](https://github.com/dcramer))
- change API URL in get_camera_list function
([#15](https://github.com/danielfernau/unifi-protect-video-downloader/issues/15) by
[@danielfernau](https://github.com/danielfernau))
- make video file names more readable
([#23](https://github.com/danielfernau/unifi-protect-video-downloader/pull/23) by
[@danielfernau](https://github.com/danielfernau))
- change top level signature to be `protect-archiver download [--options] [dest]`
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10) by
[@dcramer](https://github.com/dcramer))
- replace accessKey authorization with Bearer Token Authorization header
([#20](https://github.com/danielfernau/unifi-protect-video-downloader/pull/20) by
[@danielfernau](https://github.com/danielfernau))
- update README to include more useful information, badges and links
([#28](https://github.com/danielfernau/unifi-protect-video-downloader/pull/28) by
[@danielfernau](https://github.com/danielfernau))

### Removed
- remove download counting
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10) by
[@dcramer](https://github.com/dcramer))
- remove auto-reauth on failure
([#10](https://github.com/danielfernau/unifi-protect-video-downloader/pull/10) by
[@dcramer](https://github.com/dcramer))


## [1.1.1] - 2019-11-30
### Fixed
- fix "First time range is negative if start time doesn't start at 0 minutes"
([#2](https://github.com/danielfernau/unifi-protect-video-downloader/issues/2) by
[@danielfernau](https://github.com/danielfernau))


## [1.1.0] - 2019-11-09
### Added
- add option to download `.jpg` snapshots using `--snapshot` (see README)
([807a320](https://github.com/danielfernau/unifi-protect-video-downloader/commit/807a320e5ba041424291369ca00c1a669e4cba8d) by
[@danielfernau](https://github.com/danielfernau))
- add exit code `6` to indicate that either the `--snapshot` or the `--start` and `--end` command line arguments are missing
([807a320](https://github.com/danielfernau/unifi-protect-video-downloader/commit/807a320e5ba041424291369ca00c1a669e4cba8d) by
[@danielfernau](https://github.com/danielfernau))

### Changed
- use `dateutil.parser` instead of `datetime.strptime` to parse start and end timestamps
([807a320](https://github.com/danielfernau/unifi-protect-video-downloader/commit/807a320e5ba041424291369ca00c1a669e4cba8d) by
[@danielfernau](https://github.com/danielfernau))
- use `timestamp()` instead of `strftime("%s")` to get unix timestamp
([807a320](https://github.com/danielfernau/unifi-protect-video-downloader/commit/807a320e5ba041424291369ca00c1a669e4cba8d) by
[@danielfernau](https://github.com/danielfernau))


## [1.0.0] - 2019-11-09
### Added
- main.py
([3909169](https://github.com/danielfernau/unifi-protect-video-downloader/commit/3909169e802546d1056e92b73315098b0ec08895) by
[@danielfernau](https://github.com/danielfernau))
- requirements.txt
([3909169](https://github.com/danielfernau/unifi-protect-video-downloader/commit/3909169e802546d1056e92b73315098b0ec08895) by
[@danielfernau](https://github.com/danielfernau))
- README
([b0ee60a](https://github.com/danielfernau/unifi-protect-video-downloader/commit/b0ee60a52dbeeaec3cc75d717f5ed49e1c55cc09) by
[@danielfernau](https://github.com/danielfernau))
- LICENSE
([a269a6e](https://github.com/danielfernau/unifi-protect-video-downloader/commit/a269a6e24394917c6810e931e72fa5a355848d84) by
[@danielfernau](https://github.com/danielfernau))
