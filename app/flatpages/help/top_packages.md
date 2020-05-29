title: Top Packages Algorithm

## Score

A package's score is currently equal to a pseudo rolling average of downloads.
In the future, a package will also gain score through reviews.

## Pseudo rolling average of downloads

Every package loses 5% of its score every day.

An open source package will gain 1 score for each unique download,
whereas a non-free package will only gain 0.1 score.

This metric aims to be roughly equivalent to the average downloads.

## Seeded using a legacy heuristic

The scoring system was seeded (ie: the scores were initially set to) 20% of an
arbitrary legacy heuristic that was previously used to rank packages.

This legacy heuristic is as follows:

	forum_score = views / max(years_since_creation, 2 weeks) + 80*clamp(months, 0.5, 6)
	forum_bonus = views + posts

	multiplier = 1
	if no screenshot:
		multiplier *= 0.8
	if not foss:
		multiplier *= 0.1

	score = multiplier * (max(downloads, forum_score * 0.6) + forum_bonus)

As said, this legacy score is no longer used when ranking mods.
It was only used to provide an initial score for the rolling average,
which was 20% of the above value.

## Manual adjustments

The admin occasionally reduces all packages by a set percentage to speed up
convergence. Convergence is when

## Transparency and Feedback

You can see all scores using the [scores REST API](/api/scores/), or by
using the [Prometheus metrics](/help/metrics/) endpoint.

Consider [suggesting improvements](https://github.com/minetest/contentdb/issues/new?assignees=&labels=Policy&template=policy.md&title=).