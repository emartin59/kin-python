from typing import Optional

from agora.model.invoice import Invoice


class Earn(object):
    """The :class:`Earn <Earn>` object, which represents an earn payment that will get submitted.

    :param destination: The public key, in raw bytes, of the account the earn will be sent to.
    :param quarks: The amount being sent.
    :param invoice: (optional) An :class:`Invoice <agora.invoice.Invoice>` object to associate with this earn.
    """

    def __init__(self, destination: bytes, quarks: int, invoice: Optional[Invoice] = None):
        self.destination = destination
        self.quarks = quarks
        self.invoice = invoice

    def __eq__(self, other):
        if not isinstance(other, Earn):
            return False

        return (self.destination == other.destination and
                self.quarks == other.quarks and
                self.invoice == other.invoice)