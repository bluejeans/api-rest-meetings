//
// AnalyticsFeedbackCommentsComments.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct AnalyticsFeedbackCommentsComments: Codable {

    /** The comment rating left by the user. */
    public var qualarooFeedback: String?
    /** The UUID of the meeting. */
    public var meetingUuid: String?
    public var callguid: String?
    /** The comment left by the user. */
    public var qualarooComments: String?

    public init(qualarooFeedback: String?, meetingUuid: String?, callguid: String?, qualarooComments: String?) {
        self.qualarooFeedback = qualarooFeedback
        self.meetingUuid = meetingUuid
        self.callguid = callguid
        self.qualarooComments = qualarooComments
    }

    public enum CodingKeys: String, CodingKey { 
        case qualarooFeedback = "qualaroo_feedback"
        case meetingUuid = "meeting_uuid"
        case callguid
        case qualarooComments = "qualaroo_comments"
    }


}

