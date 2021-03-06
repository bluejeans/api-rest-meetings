//
// AnalyticsRoiData.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct AnalyticsRoiData: Codable {

    public var roiRanges: [AnalyticsRoiDataRoiRanges]?

    public init(roiRanges: [AnalyticsRoiDataRoiRanges]?) {
        self.roiRanges = roiRanges
    }

    public enum CodingKeys: String, CodingKey { 
        case roiRanges = "roi_ranges"
    }


}

