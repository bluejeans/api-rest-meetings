//
// PersonalMeetingRoom.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct PersonalMeetingRoom: Codable {

    /** This is a unique number that is associated with the personal meeting room. */
    public var _id: Int?
    /** This is a unique guid used in BlueJeans cloud that is associated with the personal meeting room. */
    public var uuid: String?
    /** This is the name associated with personal room. */
    public var title: String?
    /** This is a short descriptive text for the personal meeting room. */
    public var _description: String?
    /** This is the epoch-based starting time (in milliseconds) of the personal meeting. */
    public var start: Int64?
    /** This is the epoch-based ending time (in milliseconds) of the personal meeting. */
    public var end: Int64?
    /** This is the unix timezone string describing the timezone for the meeting */
    public var timezone: String?
    public var advancedMeetingOptions: PersonalMeetingRoomAdvancedMeetingOptions?
    /** this property is not used in the BlueJeans Meetings product */
    public var notificationUrl: String?
    /** this property is not used in the BlueJeans Meetings product */
    public var notificationData: String?
    public var moderator: PersonalMeetingRoomModerator?
    /** This is the number that a participant would enter when joining this meeting. */
    public var numericMeetingId: String?
    /** This is a passcode that must be provided by people joining the meeting. */
    public var attendeePasscode: String?
    /** If set, causes BlueJeans to require participants to enter a passcode in order to join the meeting. */
    public var addAttendeePasscode: Bool?
    /** If set, indicates that this meeting has been deleted. */
    public var deleted: Bool?
    /** If set allows clients to send and receive 720p video resolution. */
    public var allow720p: Bool?
    /** This string indicates the meeting&#39;s operational status. */
    public var status: String?
    /** If set the meeting has been locked, and future attendees require a member to allow them to join. */
    public var locked: Bool?
    /** Internal tracking number */
    public var sequenceNumber: Int?
    /** Internal tracking number */
    public var icsUid: String?
    /** This string is the name of the type of scheduling entity. */
    public var endPointType: String?
    /** This is a string that describes the version number of the endpoint type. */
    public var endPointVersion: String?
    public var attendees: [PersonalMeetingRoomAttendees]?
    /** If set indicates that this meeting will have a large */
    public var isLargeMeeting: Bool?
    /** This is the date and time (in milliseconds) when the meeting was created. */
    public var created: Int64?
    /** This is the date and time (in milliseconds) when the meeting was last changed. */
    public var lastModified: Int64?
    /** If set indicates that the meeting has expired. */
    public var isExpired: Bool?
    /** This is a unique number associated with the first meeting in a series of meetings. */
    public var parentMeetingId: Int?
    /** This is the guid for the first meeting in a series of meetings. */
    public var parentMeetingUUID: String?
    /** This is a unique number associated with the next in a chain of meetings. */
    public var nextOccurrence: Int?
    /** This field, if set, indicates that this meeting is continously running. */
    public var timelessMeeting: Bool?
    /** This field, if set, indicates that there is no end of recurring meetings. */
    public var endlessMeeting: Bool?
    public var first: PersonalMeetingRoomFirst?
    public var last: PersonalMeetingRoomLast?
    public var next: PersonalMeetingRoomNext?
    /** This is the epoch-based starting time for the next in chain of meetings. */
    public var nextStart: Int64?
    /** This is the epoch-based ending time for the next in chain of meetings. */
    public var nextEnd: Int64?
    /** if set, indicates that this ia personal meeting. */
    public var isPersonalMeeting: Bool?
    /** How Invitee should join */
    public var inviteeJoinOption: Int?

    public init(_id: Int?, uuid: String?, title: String?, _description: String?, start: Int64?, end: Int64?, timezone: String?, advancedMeetingOptions: PersonalMeetingRoomAdvancedMeetingOptions?, notificationUrl: String?, notificationData: String?, moderator: PersonalMeetingRoomModerator?, numericMeetingId: String?, attendeePasscode: String?, addAttendeePasscode: Bool?, deleted: Bool?, allow720p: Bool?, status: String?, locked: Bool?, sequenceNumber: Int?, icsUid: String?, endPointType: String?, endPointVersion: String?, attendees: [PersonalMeetingRoomAttendees]?, isLargeMeeting: Bool?, created: Int64?, lastModified: Int64?, isExpired: Bool?, parentMeetingId: Int?, parentMeetingUUID: String?, nextOccurrence: Int?, timelessMeeting: Bool?, endlessMeeting: Bool?, first: PersonalMeetingRoomFirst?, last: PersonalMeetingRoomLast?, next: PersonalMeetingRoomNext?, nextStart: Int64?, nextEnd: Int64?, isPersonalMeeting: Bool?, inviteeJoinOption: Int?) {
        self._id = _id
        self.uuid = uuid
        self.title = title
        self._description = _description
        self.start = start
        self.end = end
        self.timezone = timezone
        self.advancedMeetingOptions = advancedMeetingOptions
        self.notificationUrl = notificationUrl
        self.notificationData = notificationData
        self.moderator = moderator
        self.numericMeetingId = numericMeetingId
        self.attendeePasscode = attendeePasscode
        self.addAttendeePasscode = addAttendeePasscode
        self.deleted = deleted
        self.allow720p = allow720p
        self.status = status
        self.locked = locked
        self.sequenceNumber = sequenceNumber
        self.icsUid = icsUid
        self.endPointType = endPointType
        self.endPointVersion = endPointVersion
        self.attendees = attendees
        self.isLargeMeeting = isLargeMeeting
        self.created = created
        self.lastModified = lastModified
        self.isExpired = isExpired
        self.parentMeetingId = parentMeetingId
        self.parentMeetingUUID = parentMeetingUUID
        self.nextOccurrence = nextOccurrence
        self.timelessMeeting = timelessMeeting
        self.endlessMeeting = endlessMeeting
        self.first = first
        self.last = last
        self.next = next
        self.nextStart = nextStart
        self.nextEnd = nextEnd
        self.isPersonalMeeting = isPersonalMeeting
        self.inviteeJoinOption = inviteeJoinOption
    }

    public enum CodingKeys: String, CodingKey { 
        case _id = "id"
        case uuid
        case title
        case _description = "description"
        case start
        case end
        case timezone
        case advancedMeetingOptions
        case notificationUrl
        case notificationData
        case moderator
        case numericMeetingId
        case attendeePasscode
        case addAttendeePasscode
        case deleted
        case allow720p
        case status
        case locked
        case sequenceNumber
        case icsUid
        case endPointType
        case endPointVersion
        case attendees
        case isLargeMeeting
        case created
        case lastModified
        case isExpired
        case parentMeetingId
        case parentMeetingUUID
        case nextOccurrence
        case timelessMeeting
        case endlessMeeting
        case first
        case last
        case next
        case nextStart
        case nextEnd
        case isPersonalMeeting
        case inviteeJoinOption
    }


}

