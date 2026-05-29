id="jlwmdd"
class Deduplicator:

    @staticmethod
    def remove_duplicates(elements):

        unique = []

        seen = set()

        for el in elements:

            key = (
                el.get("locator"),
                el.get("tag")
            )

            if key not in seen:

                seen.add(key)

                unique.append(el)

        return unique

