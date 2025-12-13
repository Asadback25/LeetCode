# LeetCode
# 3606. Coupon Code Validator / Easy

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def is_valid_code(coupon_code: str) -> bool:

            if not coupon_code:
                return False

            for char in coupon_code:
                if not (char.isalpha() or char.isdigit() or char == "_"):
                    return False

            return True

        valid_business_lines = {"electronics", "grocery", "pharmacy", "restaurant"}

        valid_indices = []

        for index, (coupon_code, business, is_active_flag) in enumerate(
                zip(code, businessLine, isActive)
        ):

            if (is_active_flag and
                    business in valid_business_lines and
                    is_valid_code(coupon_code)):
                valid_indices.append(index)

        valid_indices.sort(key=lambda i: (businessLine[i], code[i]))

        return [code[i] for i in valid_indices]