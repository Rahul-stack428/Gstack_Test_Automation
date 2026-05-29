
class WaitEngine:

    @staticmethod
    def wait_after_click(page):

        page.wait_for_load_state("networkidle")

    @staticmethod
    def wait_for_spinner(page):

        spinner_selectors = [
            ".spinner",
            ".loader",
            ".loading",
            ".MuiCircularProgress-root"
        ]

        for selector in spinner_selectors:

            try:
                page.locator(selector).wait_for(
                    state="hidden",
                    timeout=3000
                )
            except:
                pass

    @staticmethod
    def wait_for_table(page):

        try:
            page.locator("table").first.wait_for(
                state="visible",
                timeout=5000
            )
        except:
            pass

    @staticmethod
    def smart_wait(page):

        WaitEngine.wait_after_click(page)
        WaitEngine.wait_for_spinner(page)
