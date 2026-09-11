"""Sample support docs. MeshAPI chunks and embeds these on upload."""

KNOWLEDGE_BASE = [
    {
        "id": "doc-1",
        "title": "Trials and Refunds",
        "text": "Harbor Desk gives every new workspace a 14-day free trial. After the first paid invoice, monthly plans are not refunded mid-cycle. Annual plans can be converted to account credit for unused full months if you write to billing within 10 days of the charge.",
    },
    {
        "id": "doc-2",
        "title": "Seat Limits",
        "text": "Solo includes 3 seats, Team includes 25, and Studio is uncapped. Invites above the cap stay pending until you upgrade or someone leaves. People already in the workspace keep access; they are not kicked out when you hit the limit.",
    },
    {
        "id": "doc-3",
        "title": "Board Archive",
        "text": "Archived boards stay recoverable for 60 days, then they are purged. Closing a workspace keeps a zip export available for 45 days. Reopening inside that window restores boards that have not been purged yet.",
    },
    {
        "id": "doc-4",
        "title": "Guest Links",
        "text": "A guest link lasts 72 hours and can be revoked from the share panel at any time. Guests may comment and pin, but they cannot export or change billing. Password-protected links are available on Team and Studio only.",
    },
    {
        "id": "doc-5",
        "title": "Sign-in Methods",
        "text": "Studio workspaces must use passkeys. Team can use passkeys or an authenticator app. Solo can sign in with email magic links. Harbor Desk does not send SMS codes. Recovery keys are shown once when you add a passkey.",
    },
    {
        "id": "doc-6",
        "title": "Webhook Limits",
        "text": "Outbound webhooks are capped at 60 events per minute on Solo, 400 on Team, and a contract limit on Studio. Crossing the cap returns HTTP 429 with a Retry-After value in seconds.",
    },
    {
        "id": "doc-7",
        "title": "Plan Changes",
        "text": "Downgrades apply on the next invoice, not immediately. If you have more active seats than the new plan allows, extra members become comment-only for 10 days so you can free seats or move back up.",
    },
    {
        "id": "doc-8",
        "title": "Support Hours",
        "text": "Solo gets email replies within two business days. Team gets weekday chat from 10:00 to 18:00 in the workspace timezone. Studio includes a shared Slack channel and a two-hour first-response target.",
    },
]
